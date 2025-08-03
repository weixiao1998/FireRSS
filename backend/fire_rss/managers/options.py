from typing import Any, List, Optional

from sqlmodel import Session, select

from ..base import errors
from ..models.options import Option, OptionCreate, OptionUpdate


class OptionManager:
    def __init__(self, session):
        self.session: Session = session

    def create_option_by_data(self, option_data: OptionCreate) -> Option:
        """Create a new option"""
        # Check if key already exists
        existing_option = self.session.exec(
            select(Option).where(Option.key == option_data.key)
        ).first()
        if existing_option:
            raise errors.OptionExistsError(f"option '{option_data.key}' already exists")

        # Create option object
        option = Option(key=option_data.key, description=option_data.description)
        option.set_value(option_data.value)

        # Add to database
        self.session.add(option)
        self.session.commit()
        return option

    def create_option(self, key: str, value: Any, description: str = "") -> Option:
        """Create a new option"""
        option_data = OptionCreate(key=key, value=value, description=description)
        return self.create_option_by_data(option_data)

    def get_option(self, key: str) -> Option:
        """Get option by key"""
        option = self.session.exec(select(Option).where(Option.key == key)).first()
        if not option:
            raise errors.OptionNotFoundError(f"option '{key}' not found")
        return option

    def get_option_value(self, key: str) -> Any:
        """Get option value (with automatic type conversion)"""
        option = self.get_option(key)
        return option.get_value()

    def update_option(self, key: str, option_data: OptionUpdate) -> Option:
        """Update option"""
        option = self.get_option(key)

        if option_data.value is not None:
            option.set_value(option_data.value)

        if option_data.description is not None:
            option.description = option_data.description

        self.session.commit()
        self.session.refresh(option)
        return option

    def delete_option(self, key: str) -> None:
        """Delete option"""
        option = self.get_option(key)
        self.session.delete(option)
        self.session.commit()

    def list_options(
        self, page_size: int = 100, page_num: int = 1, key: Optional[str] = None
    ) -> List[Option]:
        """List options"""
        query = select(Option)

        if key:
            query = query.where(Option.key.contains(key))

        # Add pagination
        if page_size > 0 and page_num > 0:
            query = query.offset((page_num - 1) * page_size).limit(page_size)

        return self.session.exec(query).all()
