import datetime
from app.db import db

DEFAULT_CONFIG = {
    "id": "default_config",
    "quizPassXp": 50,
    "labCompletionXp": 100,
    "dailyStreakCoins": 10,
    "arenaWinCoins": 25,
    "arenaWinXp": 30,
    "perfectQuizBonusXp": 25,
}

def format_iso(val):
    if not val:
        return None
    if hasattr(val, 'isoformat'):
        return val.isoformat()
    return str(val)

def get_system_config():
    """
    Returns the live platform gamification economy rates from Neon PostgreSQL.
    Falls back to safe default constants if table or connection is temporarily unreachable.
    """
    try:
        rows = db.query_raw('SELECT * FROM "SystemConfig" WHERE id = $1', 'default_config')
        if rows:
            cfg = rows[0]
            return {
                "id": cfg.get("id", "default_config"),
                "quizPassXp": int(cfg.get("quizPassXp", DEFAULT_CONFIG["quizPassXp"])),
                "labCompletionXp": int(cfg.get("labCompletionXp", DEFAULT_CONFIG["labCompletionXp"])),
                "dailyStreakCoins": int(cfg.get("dailyStreakCoins", DEFAULT_CONFIG["dailyStreakCoins"])),
                "arenaWinCoins": int(cfg.get("arenaWinCoins", DEFAULT_CONFIG["arenaWinCoins"])),
                "arenaWinXp": int(cfg.get("arenaWinXp", DEFAULT_CONFIG["arenaWinXp"])),
                "perfectQuizBonusXp": int(cfg.get("perfectQuizBonusXp", DEFAULT_CONFIG["perfectQuizBonusXp"])),
                "updatedAt": format_iso(cfg.get("updatedAt"))
            }

        # Seed if row does not exist
        db.execute_raw('''
            INSERT INTO "SystemConfig" ("id", "quizPassXp", "labCompletionXp", "dailyStreakCoins", "arenaWinCoins", "arenaWinXp", "perfectQuizBonusXp", "updatedAt")
            VALUES ('default_config', 50, 100, 10, 25, 30, 25, NOW())
            ON CONFLICT ("id") DO NOTHING;
        ''')
        return dict(DEFAULT_CONFIG, updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())
    except Exception as e:
        print(f"[Economy Service] Error fetching SystemConfig: {e}")
        return dict(DEFAULT_CONFIG, updatedAt=datetime.datetime.now(datetime.timezone.utc).isoformat())

def update_system_config(rates):
    """
    Updates the system configuration rates in Neon PostgreSQL with sanitization.
    """
    quiz_pass_xp = max(0, int(rates.get("quizPassXp", 50)))
    lab_completion_xp = max(0, int(rates.get("labCompletionXp", 100)))
    daily_streak_coins = max(0, int(rates.get("dailyStreakCoins", 10)))
    arena_win_coins = max(0, int(rates.get("arenaWinCoins", 25)))
    arena_win_xp = max(0, int(rates.get("arenaWinXp", 30)))
    perfect_quiz_bonus_xp = max(0, int(rates.get("perfectQuizBonusXp", 25)))

    updated = db.query_raw('''
        INSERT INTO "SystemConfig" ("id", "quizPassXp", "labCompletionXp", "dailyStreakCoins", "arenaWinCoins", "arenaWinXp", "perfectQuizBonusXp", "updatedAt")
        VALUES ('default_config', $1, $2, $3, $4, $5, $6, NOW())
        ON CONFLICT ("id") DO UPDATE SET
            "quizPassXp" = EXCLUDED."quizPassXp",
            "labCompletionXp" = EXCLUDED."labCompletionXp",
            "dailyStreakCoins" = EXCLUDED."dailyStreakCoins",
            "arenaWinCoins" = EXCLUDED."arenaWinCoins",
            "arenaWinXp" = EXCLUDED."arenaWinXp",
            "perfectQuizBonusXp" = EXCLUDED."perfectQuizBonusXp",
            "updatedAt" = NOW()
        RETURNING *;
    ''', quiz_pass_xp, lab_completion_xp, daily_streak_coins, arena_win_coins, arena_win_xp, perfect_quiz_bonus_xp)

    if updated:
        row = updated[0]
        return {
            "id": row.get("id"),
            "quizPassXp": row.get("quizPassXp"),
            "labCompletionXp": row.get("labCompletionXp"),
            "dailyStreakCoins": row.get("dailyStreakCoins"),
            "arenaWinCoins": row.get("arenaWinCoins"),
            "arenaWinXp": row.get("arenaWinXp"),
            "perfectQuizBonusXp": row.get("perfectQuizBonusXp"),
            "updatedAt": format_iso(row.get("updatedAt"))
        }
    return get_system_config()

def grant_student_reward(user_id, xp_amount, coins_amount, reason="Admin Bonus Reward"):
    """
    Safely grants manual XP / coins to a specific student.
    Recalculates student level dynamically without resetting existing balances.
    """
    user_rows = db.query_raw('SELECT id, username, email, xp, coins, level FROM "User" WHERE id = $1', user_id)
    if not user_rows:
        raise ValueError(f"Student with ID '{user_id}' not found.")

    user = user_rows[0]
    current_xp = int(user.get("xp") or 0)
    current_coins = int(user.get("coins") or 0)
    current_level = int(user.get("level") or 1)

    add_xp = int(xp_amount or 0)
    add_coins = int(coins_amount or 0)

    new_xp = max(0, current_xp + add_xp)
    new_coins = max(0, current_coins + add_coins)
    new_level = max(1, (new_xp // 100) + 1)

    updated_rows = db.query_raw('''
        UPDATE "User"
        SET xp = $1, coins = $2, level = $3
        WHERE id = $4
        RETURNING id, username, email, xp, coins, level;
    ''', new_xp, new_coins, new_level, user_id)

    updated = updated_rows[0] if updated_rows else None

    return {
        "userId": user_id,
        "username": user.get("username"),
        "email": user.get("email"),
        "xpAdded": add_xp,
        "coinsAdded": add_coins,
        "reason": reason,
        "previousXp": current_xp,
        "newXp": new_xp,
        "previousCoins": current_coins,
        "newCoins": new_coins,
        "previousLevel": current_level,
        "newLevel": new_level,
        "leveledUp": new_level > current_level
    }

def grant_bulk_reward(xp_amount, coins_amount, reason="Campus-Wide Community Grant"):
    """
    Safely grants bonus XP and Coins to all active platform users.
    Recalculates levels dynamically without any corruption.
    """
    add_xp = max(0, int(xp_amount or 0))
    add_coins = max(0, int(coins_amount or 0))

    if add_xp == 0 and add_coins == 0:
        return {"affectedUsers": 0, "message": "No XP or coins specified."}

    # Execute safe atomic increment for all users
    db.execute_raw('''
        UPDATE "User"
        SET xp = xp + $1,
            coins = coins + $2,
            level = GREATEST(1, ((xp + $1) / 100) + 1);
    ''', add_xp, add_coins)

    count_rows = db.query_raw('SELECT COUNT(*) as count FROM "User"')
    total = count_rows[0]['count'] if count_rows else 0

    return {
        "affectedUsers": total,
        "xpAdded": add_xp,
        "coinsAdded": add_coins,
        "reason": reason
    }
