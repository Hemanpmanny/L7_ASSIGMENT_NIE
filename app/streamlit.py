import streamlit as st
from main import ChocoHouseDB

# Initialize the Chocolate House Management System
choco_db = ChocoHouseDB()

# Function to show all flavors
def show_flavors():
    all_flavors = choco_db.fetch_all_flavours()
    if all_flavors:
        for flavor in all_flavors:
            st.write(f"ID: {flavor[0]}, Name: {flavor[1]}, Description: {flavor[2]}, Seasonal: {flavor[3]}, Season: {flavor[4]}")
    else:
        st.write("No flavors available.")

# Function to show all ingredients
def show_ingredients():
    all_ingredients = choco_db.fetch_all_ingredients()
    if all_ingredients:
        for ingredient in all_ingredients:
            st.write(f"ID: {ingredient[0]}, Name: {ingredient[1]}, Quantity: {ingredient[2]}, Unit: {ingredient[3]}, Allergen Info: {ingredient[4]}")
    else:
        st.write("No ingredients available.")

# Streamlit App Layout
st.title("Chocolate House Management System")

# Sidebar menu
menu_option = st.sidebar.selectbox("Choose an option", ["View Flavors", "Add Flavor", "Remove Flavor", "Manage Ingredients", "Customer Suggestions"])

# Flavor Management
if menu_option == "View Flavors":
    show_flavors()

elif menu_option == "Add Flavor":
    st.subheader("Add New Flavor")
    flavor_name = st.text_input("Flavor Name")
    flavor_desc = st.text_area("Flavor Description")
    seasonal = st.checkbox("Is Seasonal?")
    flavor_season = st.text_input("Season (if applicable)")
    if st.button("Add Flavor"):
        choco_db.insert_flavour(flavor_name, flavor_desc, seasonal, flavor_season)
        st.success(f"Flavor '{flavor_name}' added successfully!")

elif menu_option == "Remove Flavor":
    show_flavors()
    flavor_id = st.number_input("Enter the ID of the flavor to remove:", min_value=1, step=1)
    if st.button("Remove Flavor"):
        if choco_db.remove_flavour(flavor_id):
            st.success(f"Flavor with ID {flavor_id} removed successfully!")
            show_flavors()
        else:
            st.error(f"Failed to remove Flavor with ID {flavor_id}")

# Ingredient Management
elif menu_option == "Manage Ingredients":
    ingredient_option = st.radio("Select Ingredient Option", ["View Ingredients", "Add Ingredient", "Remove Ingredient", "Update Ingredient Quantity"])
    
    if ingredient_option == "View Ingredients":
        show_ingredients()

    elif ingredient_option == "Add Ingredient":
        st.subheader("Add New Ingredient")
        ingredient_name = st.text_input("Ingredient Name")
        ingredient_qty = st.number_input("Quantity", min_value=0)
        ingredient_unit = st.text_input("Unit")
        allergen_info = st.text_input("Allergen Information (optional)")
        if st.button("Add Ingredient"):
            choco_db.insert_ingredient(ingredient_name, ingredient_qty, ingredient_unit, allergen_info)
            st.success(f"Ingredient '{ingredient_name}' added successfully!")

    elif ingredient_option == "Remove Ingredient":
        show_ingredients()
        ingredient_id = st.number_input("Enter the ID of the ingredient to remove:", min_value=1, step=1)
        if st.button("Remove Ingredient"):
            if choco_db.remove_ingredient(ingredient_id):
                st.success(f"Ingredient with ID {ingredient_id} removed successfully!")
                show_ingredients()
            else:
                st.error(f"Failed to remove Ingredient with ID {ingredient_id}")

    elif ingredient_option == "Update Ingredient Quantity":
        show_ingredients()
        ingredient_id = st.number_input("Enter the ID of the ingredient to update:", min_value=1, step=1)
        new_qty = st.number_input("New Quantity", min_value=0)
        if st.button("Update Quantity"):
            if choco_db.update_ingredient_qty(ingredient_id, new_qty):
                st.success(f"Quantity for ingredient ID {ingredient_id} updated successfully!")
                show_ingredients()
            else:
                st.error(f"Failed to update quantity for ingredient ID {ingredient_id}")

# Customer Suggestions
elif menu_option == "Customer Suggestions":
    st.subheader("Customer Suggestions")
    all_suggestions = choco_db.fetch_all_suggestions()
    if all_suggestions:
        for suggestion in all_suggestions:
            st.write(f"ID: {suggestion[0]}, Flavor Name: {suggestion[1]}, Description: {suggestion[2]}, Allergen Concerns: {suggestion[3]}")
    else:
        st.write("No suggestions available.")

    suggestion_flavor_name = st.text_input("Flavor Name for Suggestion")
    suggestion_desc = st.text_area("Suggestion Description")
    suggestion_allergen_concerns = st.text_input("Allergen Concerns (optional)")
    if st.button("Add Suggestion"):
        choco_db.insert_suggestion(suggestion_flavor_name, suggestion_desc, suggestion_allergen_concerns)
        st.success(f"Suggestion for flavor '{suggestion_flavor_name}' added successfully!")