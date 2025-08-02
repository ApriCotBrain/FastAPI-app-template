"""
Template table

Revision ID: 5d47ac896e82
Revises:   # noqa: UP035
Create Date: 2025-06-29 13:26:30.133904

"""

from typing import Sequence  # noqa: UP035

import sqlalchemy as sa
from alembic import op

revision: str = "5d47ac896e82"
down_revision: str | None = None
branch_labels: str | Sequence[str] | None = None
depends_on: str | Sequence[str] | None = None


def upgrade() -> None:
    op.create_table(
        "template",
        sa.Column("name", sa.String(length=150), nullable=False),
        sa.Column("id", sa.UUID(), nullable=False),
        sa.Column("created_at", sa.DateTime(), nullable=False),
        sa.Column("updated_at", sa.DateTime(), nullable=False),
        sa.PrimaryKeyConstraint("id", name=op.f("pk_template")),
    )


def downgrade() -> None:
    op.drop_table("template")
