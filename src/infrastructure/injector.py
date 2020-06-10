from src.infrastructure.database.repositories.item import ItemRepositorySQL
from src.infrastructure.database.repositories.recipe import RecipeRepositorySQL
from src.infrastructure.database.repositories.shopping_list import ShoppingListRepositorySQL
from src.infrastructure.database.repositories.user import UserRepositorySQL
from src.usecases.add_item_to_current_list import AddItemToCurrentList
from src.usecases.archive_current_shopping_list import ArchiveCurrentShoppingList
from src.usecases.get_all_items import GetAllItems
from src.usecases.get_all_recipes import GetAllRecipes
from src.usecases.get_available_recipes import GetAvailableRecipes
from src.usecases.get_current_shopping_list import GetCurrentShoppingList
from src.usecases.get_user_by_id import GetUserById
from src.usecases.get_user_with_credentials import GetUserWithCredentials
from src.usecases.remove_item_from_current_shopping_list import RemoveItemFromCurrentShoppingList
from src.usecases.user_signup import UserSignup

user_repository = UserRepositorySQL()
user_signup = UserSignup(user_repository)
item_repository = ItemRepositorySQL()
shopping_list_repository = ShoppingListRepositorySQL()
recipre_repository = RecipeRepositorySQL()

get_user_with_credentials = GetUserWithCredentials(user_repository)
get_user_by_id = GetUserById(user_repository)

add_item_to_current_list = AddItemToCurrentList(item_repository,
                                                shopping_list_repository)

get_current_shopping_list = GetCurrentShoppingList(shopping_list_repository)

remove_item_from_current_shopping_list = RemoveItemFromCurrentShoppingList(shopping_list_repository)

get_available_recipes = GetAvailableRecipes(recipre_repository, shopping_list_repository)

get_all_items = GetAllItems(item_repository)

archive_current_shopping_list = ArchiveCurrentShoppingList(shopping_list_repository)

get_all_recipes = GetAllRecipes(recipre_repository)
