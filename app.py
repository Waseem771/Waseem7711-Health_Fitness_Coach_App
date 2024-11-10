import streamlit as st

# Function to generate a detailed diet plan based on fitness goal and diet preferences
def generate_detailed_diet_plan(fitness_goal, diet_preferences):
    if fitness_goal == 'lose weight':
        if diet_preferences == 'Keto':
            return {
                "Breakfast": "Avocado with scrambled eggs, and spinach.",
                "Lunch": "Grilled chicken salad with olive oil, avocado, and leafy greens.",
                "Dinner": "Salmon with steamed broccoli and cauliflower rice.",
                "Snacks": "Almonds or a handful of mixed nuts.",
                "Nutritional Advice": "Keep your carbohydrate intake low and focus on healthy fats and moderate proteins."
            }
        elif diet_preferences == 'Vegetarian':
            return {
                "Breakfast": "Greek yogurt with chia seeds, berries, and nuts.",
                "Lunch": "Quinoa salad with chickpeas, tomatoes, cucumber, and tahini dressing.",
                "Dinner": "Grilled tofu with steamed vegetables and a side of quinoa.",
                "Snacks": "Carrot sticks with hummus or a handful of almonds.",
                "Nutritional Advice": "Focus on plant-based proteins and fiber-rich vegetables."
            }
        else:  # Balanced diet
            return {
                "Breakfast": "Oatmeal with bananas, chia seeds, and almonds.",
                "Lunch": "Grilled chicken with mixed vegetables and brown rice.",
                "Dinner": "Baked salmon with roasted sweet potatoes and a side of greens.",
                "Snacks": "Apple slices with peanut butter or low-fat Greek yogurt.",
                "Nutritional Advice": "Ensure a good balance of protein, fiber, and healthy fats in every meal."
            }
    else:  # For muscle gain or maintenance plans (this can be expanded similarly)
        return {
            "Breakfast": "Egg whites scrambled with spinach, bell peppers, and a slice of whole-grain toast.",
            "Lunch": "Chicken breast with quinoa, steamed broccoli, and olive oil.",
            "Dinner": "Grilled fish with roasted vegetables and a side of brown rice.",
            "Snacks": "Low-fat cheese and a handful of almonds.",
            "Nutritional Advice": "Ensure each meal has high protein content to support muscle building."
        }

# Main Streamlit app function
def app():
    st.title('Health and Fitness Coach')
    st.header('Track your fitness and weight loss journey with personalized plans')

    # User profile input (name and fitness goal)
    if 'profile_created' not in st.session_state:
        st.session_state.name = st.text_input("Enter your name:")
        st.session_state.fitness_goal = st.selectbox("Select your fitness goal", ["lose weight", "gain muscle", "maintain weight"])

    # Create profile if name is entered
    if st.session_state.name:
        st.session_state.profile_created = True
        st.write(f"Profile created for {st.session_state.name}! Fitness goal: {st.session_state.fitness_goal}")
    
    # Display diet plan generation options
    if 'profile_created' in st.session_state and st.session_state.profile_created:
        st.subheader(f"Hello, {st.session_state.name}!")
        
        # Ask user to select a diet preference (Keto, Vegetarian, Balanced)
        diet_preference = st.radio("Select your diet preference:", ["Balanced", "Keto", "Vegetarian"])
        
        # Button to generate the diet plan
        if st.button("Generate Diet Plan"):
            # Generate detailed diet plan
            detailed_diet_plan = generate_detailed_diet_plan(st.session_state.fitness_goal, diet_preference)
            
            st.write("### Your Personalized Diet Plan:")
            for meal, recommendation in detailed_diet_plan.items():
                st.write(f"**{meal}:** {recommendation}")
            
            # Nutritional advice
            st.write(f"**Nutritional Advice:** {detailed_diet_plan['Nutritional Advice']}")

        # Set milestones for weight loss
        if st.button("Set Milestones"):
            weight_loss_target = st.number_input("Enter your target weight (kg):", min_value=1.0)
            if weight_loss_target:
                st.session_state.target_weight = weight_loss_target
                st.success(f"Your weight loss target is {weight_loss_target} kg!")
            else:
                st.error("Please enter a valid target weight.")
        
        # Track progress toward milestones
        if 'target_weight' in st.session_state:
            current_weight = st.number_input("Enter your current weight (kg):", min_value=1.0)
            if current_weight:
                st.write(f"Current weight: {current_weight} kg")
                if current_weight <= st.session_state.target_weight:
                    st.success(f"Congratulations! You've reached your target weight of {st.session_state.target_weight} kg!")
                else:
                    st.write(f"Your next milestone is {st.session_state.target_weight} kg.")
            else:
                st.warning("Please enter your current weight.")

# Run the Streamlit app
if __name__ == '__main__':
    app()
