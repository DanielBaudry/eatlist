from src.infrastructure.database.repositories.item import ItemRepositorySQL
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.infrastructure.database.repositories.user import UserRepositorySQL
from src.usecases.add_item_to_current_list import AddItemToCurrentList
from src.usecases.get_current_shopping_list import GetCurrentShoppingList
from src.usecases.get_user_by_id import GetUserById
from src.usecases.get_user_with_credentials import GetUserWithCredentials
from src.usecases.remove_item_from_current_shopping_list import RemoveItemFromCurrentShoppingList
from src.usecases.user_signup import UserSignup

user_repository = UserRepositorySQL()
user_signup = UserSignup(user_repository)

get_user_with_credentials = GetUserWithCredentials(user_repository)
get_user_by_id = GetUserById(user_repository)

item_repository = ItemRepositorySQL()
shopping_list_repository = ShoppingListRepositorySQL()

add_item_to_current_list = AddItemToCurrentList(item_repository,
                                                shopping_list_repository)

get_current_shopping_list = GetCurrentShoppingList(shopping_list_repository)

remove_item_from_current_shopping_list = RemoveItemFromCurrentShoppingList(shopping_list_repository)
