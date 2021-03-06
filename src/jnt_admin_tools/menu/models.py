"""
This module contains the base classes for menu and menu items.
"""
# for backward-compatibility
from jnt_admin_tools import menu
from jnt_admin_tools.deprecate_utils import import_path_is_changed
from django.conf import settings
from django.db import models

user_model = getattr(settings, "AUTH_USER_MODEL", "auth.User")


class Bookmark(models.Model):
    """
    This model represents a user created bookmark.
    """

    user = models.ForeignKey(user_model, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    title = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.title} - {self.url}"

    class Meta:
        db_table = "admin_tools_menu_bookmark"
        ordering = ("id",)


class Menu(
    import_path_is_changed(
        "jnt_admin_tools.menu.models.Menu", "jnt_admin_tools.menu.Menu"
    ),
    menu.Menu,
):
    pass


class DefaultMenu(
    import_path_is_changed(
        "jnt_admin_tools.menu.models.DefaultMenu",
        "jnt_admin_tools.menu.DefaultMenu",
    ),
    menu.DefaultMenu,
):
    pass


class MenuItem(
    import_path_is_changed(
        "jnt_admin_tools.menu.models.MenuItem",
        "jnt_admin_tools.menu.items.MenuItem",
    ),
    menu.items.MenuItem,
):
    pass


class AppListMenuItem(
    import_path_is_changed(
        "jnt_admin_tools.menu.models.AppListMenuItem",
        "jnt_admin_tools.menu.items.AppList",
    ),
    menu.items.AppList,
):
    pass


class BookmarkMenuItem(
    import_path_is_changed(
        "jnt_admin_tools.menu.models.BookmarkMenuItem",
        "jnt_admin_tools.menu.items.Bookmarks",
    ),
    menu.items.Bookmarks,
):
    pass
