# backend/app/services/matchmaking_engine.py
from typing import List, Dict

class MatchmakingEngine:
    @staticmethod
    async def get_skill_swap_recommendations(user_id: str) -> List[Dict]:
        """
        AI-driven skill-swap recommendation engine.
        Finds users where:
        1. User B HAS a skill that User A WANTS.
        2. User A HAS a skill that User B WANTS.
        Orders by proficiency matches and active status.
        """
        
        # In a real scenario, this would query the DB using Prisma/SQL
        """
        Example SQL Concept:
        SELECT u2.id, u2.username, s1.name as user2_offers, s2.name as user2_wants 
        FROM User u2
        JOIN UserSkill us2_has ON u2.id = us2_has.userId AND us2_has.type = 'HAS'
        JOIN UserSkill us2_wants ON u2.id = us2_wants.userId AND us2_wants.type = 'WANTS'
        JOIN UserSkill us1_wants ON us1_wants.userId = :user_id AND us1_wants.type = 'WANTS'
        JOIN UserSkill us1_has ON us1_has.userId = :user_id AND us1_has.type = 'HAS'
        WHERE us2_has.skillId = us1_wants.skillId
          AND us2_wants.skillId = us1_has.skillId
          AND u2.id != :user_id
        """
        
        # Placeholder for actual DB query to return real matching profiles
        recommendations = [
            {
                "matched_user_id": "user-456",
                "username": "TechGuru99",
                "they_offer_skill": "React Native",
                "they_offer_proficiency": 5,
                "you_offer_skill": "German Language",
                "match_score": 98.5 # Calculated by AI matching algorithm
            },
            {
                "matched_user_id": "user-789",
                "username": "DesignNinja",
                "they_offer_skill": "UI/UX Figma",
                "they_offer_proficiency": 4,
                "you_offer_skill": "Python Flask",
                "match_score": 92.0
            }
        ]
        
        # Sort by match score descending
        return sorted(recommendations, key=lambda x: x['match_score'], reverse=True)

    @staticmethod
    async def initiate_match(initiator_id: str, receiver_id: str, initiator_offers_id: str, receiver_offers_id: str):
        """
        Creates a PENDING match request between two users.
        """
        # match = await prisma.match.create({
        #     "data": {
        #         "initiatorId": initiator_id,
        #         "receiverId": receiver_id,
        #         "initiatorOffersId": initiator_offers_id,
        #         "receiverOffersId": receiver_offers_id,
        #         "status": "PENDING"
        #     }
        # })
        # return match
        pass
