import streamlit as st
import pandas as pd
import joblib
from sklearn.preprocessing import StandardScaler
import base64
from PIL import Image




st.set_page_config(layout="wide")
def set_custom_css():
    st.markdown("""
        <style>
        /* Main font size */
        html, body, [class*="st-"] {
            font-size: 18px; /* Adjust this value as needed */
        }
        .stTitle {
            font-size: 50px; /* Adjust the title size */
        }
        /* Increase size of headers */
        .stMarkdown h1 {
            font-size: 2.5em;
        }
        .stMarkdown h2 {
            font-size: 2em;
        }
        .stMarkdown h3 {
            font-size: 1.75em;
        }
        .stLabel {
            font-size: 5em; /* Change this to the size you prefer */
        }

        /* Adjust widget sizes */
        .stSlider, .stSelectbox, .stMultiselect {
            min-height: 50px; /* Adjust height */
        }

        /* More specific widget adjustments can go here */

        </style>
    """, unsafe_allow_html=True)

# Call this function at the beginning of your app
set_custom_css()

# Rest of your Streamlit code



# Function to convert image to base64
def image_to_base64(image_path):
    with open(image_path, 'rb') as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode()
    return encoded_string

# Function to set background image
def set_bg_from_base64(base64_string):
    page_bg_img = f"""
    <style>
    .stApp {{
        background-image: url("data:image/jpg;base64,{base64_string}");
        background-position: center;      
        background-repeat: no-repeat;     
        background-attachment: fixed;     
    }}
    </style>
    """
    st.markdown(page_bg_img, unsafe_allow_html=True)

def go_to_project_overview():
    st.session_state.page_selection = "Project Overview"

def go_to_we_can_predictor():
    st.session_state.page_selection = "weCAN Predictor"

def go_to_landing_page():
    st.session_state.page_selection = "weCAN"

def go_to_main():
    st.session_state.page_selection = "Welcome"

def custom_css_welcome():
    st.markdown("""
        <style>
        .stButton>button {
            height: 2em;     /* Increase button height */
            width: 30%;     /* Set button width to 100% of the column width */
            font-size: 0.5em;  /* Adjust font size */
            font-weight: bold;
            color: white;    /* Text color */
            border-radius: 4px; /* Rounded corners */
            background-color: black; /* Red background color */
            border-width: medium;
            border-style: solid;
            border-color: black;
        }
        .stButton>button:hover {
            background-color: white; /* Darker shade for hover state */
        }
        </style>
    """, unsafe_allow_html=True)

def custom_css_landing():
    st.markdown("""
        <style>
        .stButton>button {
            height: 2em;     /* Increase button height */
            width: 30%;     /* Set button width to 100% of the column width */
            font-size: 0.5em;  /* Adjust font size */
            font-weight: bold;
            color: #003762;    /* Text color */
            border-radius: 4px; /* Rounded corners */
            background-color: #F7CBDB; /* Red background color */
            border-width: medium;
            border-style: solid;
            border-color: #003762;
        }
        .stButton>button:hover {
            background-color: #003762; /* Darker shade for hover state */
        }
        </style>
    """, unsafe_allow_html=True)

def custom_css_other():
    st.markdown("""
        <style>
        .stButton>button {
            height: 3em;     /* Increase button height */
            width: 30%;     /* Set button width to 100% of the column width */
            font-size: 1em;  /* Adjust font size */
            font-weight: bold;
            color: #003762;    /* Text color */
            border-radius: 5px; /* Rounded corners */
            background-color: #F7CBDB; /* Red background color */
            border-width: medium;
            border-style: solid;
            border-color: #003762;
        }
        .stButton>button:hover {
            background-color: #003762; /* Darker shade for hover state */
        }
        </style>
    """, unsafe_allow_html=True)
#welcome page 

def welcome_page():
    custom_css_welcome()
    set_page_bg_color("#0B0C0E") 
    image_path = 'welcome.png'
    base64_image = image_to_base64(image_path)
    set_bg_from_base64(base64_image)


    for _ in range(80):  # Adjust 'number_of_spacer_rows' to move the button down
        st.write("")
    c1, enter_button = st.columns((2,3))  # adjust ratios for positioning

    
    # Column for button
    with enter_button:
        if st.button("## ▶️ Enter", on_click=go_to_landing_page, key='a'):
            pass


# Page functions
def landing_page():
    custom_css_landing()
    set_page_bg_color("#DCEEEF") 
    image_path = 'weCAN.jpg'
    base64_image = image_to_base64(image_path)
    set_bg_from_base64(base64_image)

    for _ in range(80):  # Adjust 'number_of_spacer_rows' to move the button down
        st.write("")
    space1, col_button, spacer = st.columns((3.5,4, 1))  # adjust ratios for positioning
    
    # Column for button
    with col_button:
         if st.button("## Project Overview", on_click=go_to_project_overview):
            pass
   

def project_overview():
    custom_css_other()
    set_page_bg_color("#DCEEEF")

    path_to_image3 = 'brainbody.jpg'  # image path
    image3 = Image.open(path_to_image3)
   
   #set columns for formatting
    col1, col2 = st.columns([1, 1])

    with col1:
        if st.button("## 🧬 weCAN Predictor", on_click=go_to_we_can_predictor, key='a'):
            pass #button to go to predictor

        title="🏔️ Project Overview"
        title_html = f"<p style='text-align:center; color: #003762; font-size: 80px;'>{title}</p>"
        st.markdown(title_html, unsafe_allow_html=True)
        # Introduction

        intro = "📖 Introduction"
        intro_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{intro}</p>"
        st.markdown(intro_html, unsafe_allow_html=True)
        st.markdown("""
        Welcome to the weCAN Predictor, a groundbreaking tool designed to 
        enhance cancer survivability predictions. 
        """)
        st.markdown("""This project leverages 
        advanced machine learning algorithms to analyze clinical data and 
        provide healthcare professionals with actionable insights.
        """)
        st.markdown("""The motivation for this project is a a personal and professional connection to cancer. Like the majority of people I have been personally, indirectly affected by cancer. 
        I also worked in clinical cancer diagnosis and detection for 7+ years and have a deep seeded interest in the field. Cancer prognosis and survivability affects patients, their friends and family, and their quality of life.
        Accuracy in prognosis predictions is very important. 
        When a patient is given a prognosis, they begin to map out the remainder of their time. When the prognosis is inaccurate, some are lucky and they are given more time but there are some that are not so lucky and are taken sooner than anticipated. Accurate prognosis can also help the currently overwhelmed and under-funded and under-staffed healthcare systems around the world. It can help with resource mangement to alloccate precious time, space and treatment resources to those who will benefit the most.
        Cancer prognosis affects everyone involved from pateints to families to health care staff and I hope to develop a model that can better predict this metric to make living with cancer better for everyone.""")

        st.markdown("---")

        # Project Goals
        goals = "🥅 Project Goals"
        goals_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{goals}</p>"
        st.markdown(goals_html, unsafe_allow_html=True)
        st.markdown("""
        The weCAN Predictor aims to:
        - **Improve Accuracy:** Utilize cutting-edge machine learning models 
        to improve the accuracy of cancer survivability predictions.
        - **Enhance Decision Making:** Provide healthcare professionals with 
        a reliable tool to assist in treatment planning and patient counseling.
        - **Data-Driven Insights:** Offer insights into critical factors affecting 
        cancer outcomes, facilitating targeted research and intervention strategies.
        """)

        st.markdown("---")

        #The Data
        data = "📊 The Data"
        data_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{data}</p>"
        st.markdown(data_html, unsafe_allow_html=True)
        
        st.markdown("""
        The data for the weCAN predictor comes from the MSK Met Study in 2021:
        - **Data Set:** Consists of 25,775 patients and 55 features.
        - **What we are predicting:** We are predicting the Prognosis Group each patient belongs to.
        """)

        st.markdown("---")

        # Methodology
        method = "🔎 Methodology"
        method_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{method}</p>"
        st.markdown(method_html, unsafe_allow_html=True)

        st.markdown("""
        The development of weCAN Predictor involved:
        - **Data Collection:** Gathering comprehensive clinical data from various 
        cancer patients, including demographics, genetic information, and disease status.
        - **Model Development:** Employing logistic regression to model survivability, 
        chosen for its interpretability and effectiveness in classification tasks.
        - **Feature Engineering:** Identifying and integrating key predictors of 
        cancer outcomes into the model to enhance its predictive power.
        -**Model Deplyment:** Build a user interface where medical professionals can input patient data and make prognostic predictions.
        """)
        
        st.markdown("---")

        # Key Features
        features = "🔑 Key Features"
        features_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{features}</p>"
        st.markdown(features_html, unsafe_allow_html=True)
        st.markdown("""
        The weCAN Predictor is equipped with:
        - **User-Friendly Interface:** An intuitive platform for easy input of patient data.
        - **Real-Time Predictions:** Instant survivability predictions based on the latest 
        machine learning algorithms.
        - **Data Visualization:** Graphical representation of prediction outcomes and 
        contributing factors for enhanced understanding.
        """)

        st.markdown("---")

        # Future Directions
        future = "⏭️ Future Steps"
        future_html = f"<p style='text-align:left; color: #003762; font-size: 60px;'>{future}</p>"
        st.markdown(future_html, unsafe_allow_html=True)
        st.markdown("""
        Looking ahead, the project will focus on:
        - **Model Refinement:** Continuous improvement of the prediction model by 
        incorporating more diverse datasets.
        - **Feature Expansion:** Adding more variables, like lifestyle factors and 
        patient-reported outcomes, for a holistic prediction approach.
        - **Collaboration:** Partnering with medical institutions for clinical validation 
        and implementation of the weCAN Predictor.
        """)
        
        st.markdown("---")

        # Additional Information and Links
        me = "🙋🏽‍♂️ Find Me"
        me_html = f"<p style='text-align:left; color: #003762; font-size: 40px;'>{me}</p>"
        st.markdown(me_html, unsafe_allow_html=True)
        st.markdown("""
        For more detailed information about this project: 
        - Please visit my 
        [GitHub Repository](https://github.com/r-kaba/weCAN-A-Cancer-Survivability-Predictor) 
        - Connect with me through [Rahim Kaba Linkedin](https://www.linkedin.com/in/rahim-kaba/)
        """)

        # st.write("Detailed overview of the project.")
        if st.button("## 🧬 weCAN Predictor", on_click=go_to_we_can_predictor, key='b'):
            pass
            #button to go to predictor
            
    #empty vertical spaces
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.image(image3)


#font styling for buttons
tabs_font_css = """
    <style>
    div[class*="stSelectbox"] label {
    font-size: 200px !important;
    font-size: 50px !important;
    font-weight: bold !important;
    color: #003762;
    background-color: #F7CBDB;
    border-radius: 5px;
    border-width: light;
    border-style: solid;
    border-color: #003762;
    padding: 5px; /* Added padding */
    margin-bottom: 5px; /* Added bottom margin */
    }

    div[class*="stSlider"] label {
    font-size: 200px;
    font-size: 50px !important;
    font-weight: bold !important;
    color: #003762;
    background-color: #F7CBDB;
    border-radius: 5px;
    border-width: light;
    border-style: solid;
    border-color: #003762;
    padding: 5px; /* Added padding */
    margin-bottom: 5px; /* Added bottom margin */
    }

    div[class*="stText"] label {
    font-size: 200px;
    font-size: 50px !important;
    font-weight: bold !important;
    color: #003762;
    background-color: #F7CBDB;
    border-radius: 5px;
    border-width: light;
    border-style: solid;
    border-color: #003762;
    padding: 5px; /* Added padding */
    margin-bottom: 5px; /* Added botto
    </style>
    """

# set initial states of input fields
def reset_values():
        st.session_state['fraction_genome_altered'] = 0.0
        st.session_state['metastatic_patient_label'] = 'No'
        st.session_state['met_count'] = 0
        st.session_state['met_site_count'] = 0
        st.session_state['msi_score'] = 0.0
        st.session_state['msi_instable_label'] = 'Stable'
        st.session_state['sample_coverage'] = 100
        st.session_state['tmb'] = 0.0
        st.session_state['tumor_purity'] = 0.0
        st.session_state['average_age'] = 1.0
        st.session_state['patient_id'] = "Enter ID"

 # image path
path_to_image1 = 'weCAN.jpg' 
image1 = Image.open(path_to_image1)

path_to_image2 = 'body.jpg'
image2 = Image.open(path_to_image2)

#making predictions
def make_predictions():
    if 'fraction_genome_altered' not in st.session_state:
        st.session_state['fraction_genome_altered'] = 0.0
    if 'metastatic_patient_label' not in st.session_state:
        st.session_state['metastatic_patient_label'] = 'No'
    if 'met_count' not in st.session_state:
        st.session_state['met_count'] = 0
    if 'met_site_count' not in st.session_state:
        st.session_state['met_site_count'] = 0
    if 'msi_score' not in st.session_state:
        st.session_state['msi_score'] = 0.0
    if 'msi_instable_label' not in st.session_state:
        st.session_state['msi_instable_label'] = 'Stable'
    if 'sample_coverage' not in st.session_state:
        st.session_state['sample_coverage'] = 100
    if 'tmb' not in st.session_state:
        st.session_state['tmb'] = 0.0
    if 'tumor_purity' not in st.session_state:
        st.session_state['tumor_purity'] = 0.0
    if 'average_age' not in st.session_state:
        st.session_state['average_age'] = 1.0
    if 'patient_id' not in st.session_state:
        st.session_state['patient_id']=""
        
    custom_css_other()
    set_page_bg_color("#DCEEEF")
    # Add prediction functionality here
    # st.title("weCAN Predictor")
    predictor = "🧬 weCAN Predictor 🧬 "
    predictor_html = f"<p style='text-align:left; color: #003762; font-size: 80px;'>{predictor}</p>"
    st.markdown(predictor_html, unsafe_allow_html=True)

    # Load the logistic regression model and scaler
    model = joblib.load('logreg_best_model.pkl')
    scaler = joblib.load('scaler.pkl')

  #processing data 
    def preprocess_input(data):
        # Function to preprocess and scale input data
        scaled_data = scaler.transform(data)
        return scaled_data

    #create dictionary for bool values
    metastatic_patient_options = {'Yes': 1, 'No': 0}
    msi_instable_options = {'Instable': 1, 'Stable': 0}

    st.write(tabs_font_css, unsafe_allow_html=True)

    
    #Define initial widget states 
    initial_states = {
        'fraction_genome_altered': 0.0,
        'metastatic_patient_label': 'Yes',  # 0 for No, 1 for Yes
        'met_count': 0,
        'met_site_count': 0,
        'msi_score': 0.0,
        'msi_instable_label': 'Instable',  # 0 for Stable, 1 for Instable
        'sample_coverage': 100,
        'tmb': 0.0,
        'tumor_purity': 0.0,
        'average_age': 1.0,
        'patient_id': ""
    }
    for key, value in initial_states.items():
        if key not in st.session_state:
            st.session_state[key] = value
    
    # Create columns for input fields
    col1, col2 = st.columns([1, 1])
    
    #widgets
    with col1:
        st.markdown("""# Patient Information""")
        st.session_state['patient_id'] = st.text_input('## Patient ID', value=st.session_state['patient_id'], placeholder='Enter ID')       
        st.session_state['average_age'] = st.slider('## Patient Age', min_value=1.0, max_value=100.0, step=1.0, value=st.session_state['average_age'])
        st.markdown("---")
        
        st.markdown("""# Patient Disease Status""")
        metastatic_patient_labels = list(metastatic_patient_options.keys())
        metastatic_patient_index = metastatic_patient_labels.index(st.session_state['metastatic_patient_label'])
        st.session_state['metastatic_patient_label'] = st.selectbox('## Does the Patient Have Metastatic Disease?', list(metastatic_patient_options.keys()), index=metastatic_patient_index)
        st.session_state['met_count'] = st.selectbox('## Number of Metastases', range(0, 51), index=st.session_state['met_count'])
        st.session_state['met_site_count'] = st.selectbox('## Number of Metastatic Sites', range(0, 51), index=st.session_state['met_site_count'])
        st.markdown("---")
        st.image(image1)
        
 #2nd column widgets for easier readability            
    with col2:
        st.markdown("")
        st.markdown("")
        st.markdown("")
        st.image(image2)
        st.markdown("---")
        st.markdown("")
        st.markdown("""# Cancer Genetics Information""")
        msi_instable_labels = list(msi_instable_options.keys())
        msi_instable_index = msi_instable_labels.index(st.session_state['msi_instable_label'])
        st.session_state['msi_instable_label'] = st.selectbox('## MSI Status', list(msi_instable_options.keys()), index=msi_instable_index)
        st.session_state['msi_score'] = st.slider('## MSI Score', min_value=0.0, max_value=100.0, step=0.1, value=st.session_state['msi_score'], )
        st.session_state['tmb'] = st.slider('## Tumor Mutational Burden', min_value=0.0, max_value=1000.0, step=1.0, value=st.session_state['tmb'])
        st.session_state['tumor_purity'] = st.slider('## Tumor Purity', min_value=0.0, max_value=100.0, step=5.0, value=st.session_state['tumor_purity'])
        st.session_state['fraction_genome_altered'] = st.slider('## Fraction Genome Altered', min_value=0.0, max_value=1.0, step=0.01, value=st.session_state['fraction_genome_altered'])
        # msi_instable_index = 0 if msi_instable_options[st.session_state['msi_instable_label']] == 0 else 1
        # st.session_state['msi_instable_label'] = st.selectbox('MSI Status', list(msi_instable_options.keys()), index=msi_instable_index)
       
        # st.session_state['msi_instable_label'] = msi_instable_labels[st.selectbox('MSI Status', range(len(msi_instable_labels)), index=msi_instable_index)]
        st.session_state['sample_coverage'] = st.selectbox('## Sample Coverage', range(100, 3000, 50), index=st.session_state['sample_coverage'] // 50 - 2) # Adjust the index calculation based on your range and step values
        
        #st.session_state['average_age'] = st.slider('## Patient Age', min_value=18.0, max_value=90.0, step=0.5, value=st.session_state['average_age'])

    #recode the bool values to 1 and 0
    metastatic_patient = metastatic_patient_options[st.session_state['metastatic_patient_label']]
    msi_instable = msi_instable_options[st.session_state['msi_instable_label']] 

    #add a separator
    st.markdown("---")

    # Prediction button and definition of what it does
    if st.button('## 🔎 Predict'):

        average_age = st.session_state['average_age']
        fraction_genome_altered = st.session_state['fraction_genome_altered']
        metastatic_patient = metastatic_patient_options[st.session_state['metastatic_patient_label']]
        met_count = st.session_state['met_count']
        met_site_count = st.session_state['met_site_count']
        msi_score = st.session_state['msi_score']
        msi_instable = msi_instable_options[st.session_state['msi_instable_label']]
        sample_coverage = st.session_state['sample_coverage']
        tmb = st.session_state['tmb']
        tumor_purity = st.session_state['tumor_purity']

        input_data = pd.DataFrame([[average_age, average_age, fraction_genome_altered, metastatic_patient, met_count, met_site_count, msi_score, msi_instable, sample_coverage, tmb, tumor_purity, average_age]],
                                columns=['Age at Sequencing', 'Age at Surgical Procedure','Fraction Genome Altered', 'Metastatic patient', 'Met Count', 'Met Site Count', 'MSI Score', 'MSI Instable', 'Sample coverage', 'TMB (nonsynonymous)', 'Tumor Purity', 'Average Age'])

        processed_data = preprocess_input(input_data)
        prediction = model.predict(processed_data)[0]
        prognosis_categories = {1: 'Very Poor', 2: 'Poor', 3: 'Intermediate', 4: 'Good'}
        st.write(f"Prognosis Category for Patient: {prognosis_categories[prediction]}")
    
    st.markdown("<br>", unsafe_allow_html=True)
    
    # if st.button("## ⏮️ Reset", on_click=reset_values):
    #     pass

     # Reset button
    if st.button("## ⏮️ Reset"):
        for key, value in initial_states.items():
            st.session_state[key] = value
    
    #formatting
    st.markdown("<br>", unsafe_allow_html=True)
    
    #home button
    if st.button("## 🏠 Main Page", on_click=go_to_main, key='b'):
        pass

#

# Main function for page routing
def main():
    # Set the initial state to "Welcome" if it's not already set
    if 'page_selection' not in st.session_state:
        st.session_state.page_selection = "Welcome"

    

    # Page routing based on the current state
    if st.session_state.page_selection == "Welcome":
        welcome_page()
    elif st.session_state.page_selection == "weCAN":
        landing_page()
    elif st.session_state.page_selection == "Project Overview":
        project_overview()
    elif st.session_state.page_selection == "weCAN Predictor":
        make_predictions()


#formatting

def set_page_bg_color(hex_color):
    """
    A function to set the background color of a Streamlit page.
    """
    st.markdown(
        f"""
        <style>
        .stApp {{
            background-color: {hex_color};
        }}
        </style>
        """,
        unsafe_allow_html=True
    )
# Run the app
main()



















# # Function to convert image to base64
# def image_to_base64(image_path):
#     with open(image_path, 'rb') as image_file:
#         encoded_string = base64.b64encode(image_file.read()).decode()
#     return encoded_string

# # Function to set background image
# def set_bg_from_base64(base64_string):
#     page_bg_img = f"""
#     <style>
#     .stApp {{
#         background-image: url("data:image/jpg;base64,{base64_string}");
        
#         background-position: center;      /* Center the image */
#         background-repeat: no-repeat;     /* Do not repeat the image */
#         background-attachment: fixed;     /* Optional: set the image fixed during scroll */
#     }}
#     </style>
#     """
#     st.markdown(page_bg_img, unsafe_allow_html=True)

# def landing_page():

#     # Set background for landing page
#     image_path = 'weCAN.jpg'  # Replace with your local image filename
#     base64_image = image_to_base64(image_path)
#     set_bg_from_base64(base64_image)

#     # Rest of your landing page code
#     if st.button("Project Overview"):
#         st.session_state.page = 'Project Overview'
#         #display_current_page()
#         #overview_page()
        

# # # Function for Landing Page
# # def landing_page():
# #     st.title("Welcome The weCAN Cancer Survivability Predictor")
# #     if st.button("Project Overview"):
# #         st.session_state.page = 'Project Overview'
# #         #st.experimental_rerun()

# # Function for Project Overview Page
# def overview_page():
#     st.title("weCAN Predictor: Project Overview")
#     st.write("Here is the overview of the project...")
#     if st.button("Go to weCAN Predictor Demo"):
#         st.session_state.page = 'Product Demo'
#         #demo_page()
        
#         #st.experimental_rerun()

# def demo_page():
#     st.title("weCAN Predictor Demo")

#     # Load the logistic regression model and scaler
#     model = joblib.load('logreg_best_model.pkl')
#     scaler = joblib.load('scaler.pkl')

#     def preprocess_input(data):
#         # Function to preprocess and scale input data
#         scaled_data = scaler.transform(data)
#         return scaled_data
    
#     #create dictionary for bool values
#     metastatic_patient_options = {'Yes': 1, 'No': 0}
#     msi_instable_options = {'Instable': 1, 'Stable': 0}

#     # Create columns for input fields
#     col1, col2 = st.columns(2)

#     with col1:
#         # Place your first set of inputs in the first column
#         fraction_genome_altered = st.slider('Fraction Genome Altered', min_value=0.0, max_value=1.0, step=0.01)
#         metastatic_patient_label = st.selectbox('Metastatic Patient', options=list(metastatic_patient_options.keys()))
#         #metastatic_patient = st.selectbox('Metastatic Patient', [0, 1])
#         met_count = st.selectbox('Met Count', range(0, 32, 1))
#         met_site_count = st.selectbox('Met Site Count',range(0, 16, 1))
#         msi_score = st.slider('MSI Score', min_value=0.0, max_value=53.0, step=0.1)

#     with col2:
#         # Place your second set of inputs in the second column
        
#         msi_instable_label = st.selectbox('MSI Instable', options=list(msi_instable_options.keys()))
#         #msi_instable = st.selectbox('MSI Instable', [0, 1])  # Notice the label change to avoid duplicate widget key error
#         sample_coverage = st.selectbox('Sample Coverage', range(100,2850, 50))
#         tmb = st.slider('TMB (nonsynonymous)', min_value=0.0, max_value=655.0, step=0.1)
#         tumor_purity = st.slider('Tumor Purity', min_value=0.0, max_value=100.0, step=5.0)
#         average_age =  st.slider('Average Age', min_value=18.0, max_value=90.0, step=0.5)
    
#     #recode the bool values to 1 and 0
#     metastatic_patient = metastatic_patient_options[metastatic_patient_label]
#     msi_instable = msi_instable_options[msi_instable_label]

#     # Prediction button
#     if st.button('Predict'):
#         input_data = pd.DataFrame([[average_age, average_age, fraction_genome_altered, metastatic_patient, met_count, met_site_count, msi_score, msi_instable, sample_coverage, tmb, tumor_purity, average_age]],
#                                   columns=['Age at Sequencing', 'Age at Surgical Procedure','Fraction Genome Altered', 'Metastatic patient', 'Met Count', 'Met Site Count', 'MSI Score', 'MSI Instable', 'Sample coverage', 'TMB (nonsynonymous)', 'Tumor Purity', 'Average Age'])

#         processed_data = preprocess_input(input_data)
#         prediction = model.predict(processed_data)[0]
#         prognosis_categories = {1: 'Very Poor', 2: 'Poor', 3: 'Intermediate', 4: 'Good'}
#         st.write(f"Prognosis Category: {prognosis_categories[prediction]}")



# # Initialize session state
# if 'page' not in st.session_state:
#     st.session_state.page = 'Landing Page'

# # # Sidebar for navigation
# # st.sidebar.title('Navigation')
# # sidebar_page = st.sidebar.radio("Go to", ('Landing Page', 'Project Overview', 'Product Demo'))

# # # Synchronize sidebar with session state
# # if sidebar_page != st.session_state.page:
# #     st.session_state.page = sidebar_page
# #     st.experimental_rerun()

# # st.sidebar.title('Navigation')
# # sidebar_page = st.sidebar.radio("Go to", ('Landing Page', 'Project Overview', 'Product Demo'))

# # if sidebar_page != st.session_state.page:
# #     st.session_state.page = sidebar_page 

# # Display pages based on session state

# def display_current_page():
#     # page = sidebar_content()
#     if st.session_state.page == 'Landing Page':
#         landing_page()
#     elif st.session_state.page == 'Project Overview':
#         overview_page()
#     elif st.session_state.page == 'Product Demo':
#         demo_page()

# display_current_page()