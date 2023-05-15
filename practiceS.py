import streamlit as st


def main():
    st.title("My Streamlit App")
    st.button("Click me!")
    st.header("Header")
    st.subheader("Subheader")
    st.text("Some text.")
    import pandas as pd
    df = pd.DataFrame({"Column 1": [1, 2, 3], "Column 2": [4, 5, 6]})
    st.dataframe(df)
    import matplotlib.pyplot as plt
    plt.plot([1, 2, 3], [4, 5, 6])
    st.pyplot()
    option = st.selectbox("Select an option", ["Option 1", "Option 2", "Option 3"])
    st.write("You selected:", option)
    # pie chart
   
    import matplotlib.pyplot as plt

    # Sample data
    labels = ['Apples', 'Oranges', 'Bananas']
    sizes = [30, 40, 20]

    # Create a pie chart
    fig, ax = plt.subplots()
    ax.pie(sizes, labels=labels, autopct='%1.1f%%')
    # ax.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle

    # Display the chart in Streamlit
    st.pyplot(fig)


if __name__ == "__main__":
    main()