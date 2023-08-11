# acc-fs-code-practice-many-to-many

## Instructions

**Note** If the migration fails, delete the `migrations/versions/da2d67824548_create_tables` file and run `alembic revision --autogenerate -m "create tables`

1. Add the `recipe_ingredients` join table to the `models.py file`.

2. Give each `Recipe` a way to refer to the `ingredients` that are associated with it. 

3. Give each `Ingredient` a way to refer to the `recipes` that are associated with it.

4. Test the relationship in the `seeds.py` file. 