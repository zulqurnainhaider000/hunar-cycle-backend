import os
import shutil
from pathlib import Path
from dotenv import load_dotenv

load_dotenv()

# Ensure packaged schema exists and is not empty
try:
    import prisma
    pkg_dir = Path(prisma.__file__).parent
    pkg_schema = pkg_dir / "schema.prisma"
    local_schema = Path(__file__).resolve().parent.parent / "schema.prisma"
    if local_schema.exists():
        shutil.copyfile(local_schema, pkg_schema)
except Exception as _e:
    pass

from prisma import Prisma

# Initialize a global Prisma client
db = Prisma()
