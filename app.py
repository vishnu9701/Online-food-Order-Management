import streamlit as st 
from database import*
import pandas as pd 
import time 

st.set_page_config(page_title='Order Food Now !', page_icon=None, layout="centered", initial_sidebar_state="auto", menu_items=None)

headerSection = st.container()
mainSection = st.container()
loginSection = st.container()
logOutSection = st.container()
checkoutSection = st.container()
   
food_list=[]
qty_list=[]
amt_list=[]

order = {
    'Food Name':food_list,
    'Qty' : qty_list,
    'Amount':amt_list
}

cart = pd.DataFrame(order)

def order_pressed(user_id, total_amt, paymentmethod ,food_list, qty_list):
    if place_order(user_id, total_amt, paymentmethod, food_list, qty_list):
        st.session_state['checkout'] = True
        st.session_state['loggedIn'] = False

def show_checkout_page():
    with checkoutSection:
        my_bar = st.progress(0)
        for percent_complete in range(100):
            time.sleep(0.01)
            my_bar.progress(percent_complete + 1)
        st.success(f"Hey {st.session_state['details'][1]}, Your Order has been placed Successfully")
        st.balloons()
        st.subheader(f"Your Order will arrive to your address = {st.session_state['details'][2]}")
        st.subheader(f"and our rider will contact you on = {st.session_state['details'][3]}")
        
def update_user_details(user_id, email, name ,address, number):
    if update_details(user_id, email, name ,address, number):
        st.info("User Information Updated Successfully, you will be logged out now")
        LoggedOut_Clicked()
    else:
        st.info("Error Detected while updating")


def update_user_password(user_id, password):
    if update_password(user_id, password):
        st.info("Password updated successfully, you will be logged out now")
        LoggedOut_Clicked()
    else:
        st.info("Eroor Detected while updating password")
    

def show_main_page():
    with mainSection:
        st.header(f" Welcome {st.session_state['details'][1]} :sunglasses:")
        menu, cart, myaccount = st.tabs(['Menu', 'Cart', 'My Account'])
        
        with menu:
            
            st.subheader('select the Food you want to order')
            
            col1, col2, col3 = st.columns(3)
            col1.image('images/chole.jpg',width=200)
            col1.success("Chole Bhature ")
            if col1.checkbox('@ ₹199',key =1):
                col1.warning('Enter QTY. -')
                food = col1.number_input(label="food", min_value=1,key=11)
                food_list.append('Chole Bhature')
                qty_list.append(int(food))
                amt_list.append(int(food)*199)
                      
            col2.image('images/samosa.jpg',width=200)
            col2.success("Samosa ")
            if col2.checkbox('@ ₹99',key =2):
                col2.warning('Enter QTY. -')
                food = col2.number_input(label="food", min_value=1,key=12)
                
                food_list.append('Samosa')
                qty_list.append(int(food))
                amt_list.append(int(food)*99)             
                       
            col3.image('images/gulabjamun.jpg',width=200)
            col3.success("Gulab Jamun")
            if col3.checkbox('@ ₹149',key =3):
                col3.warning('Enter QTY. -')
                food = col3.number_input(label="Gulab Jamun", min_value=1,key=13)
                food_list.append('Gulab Jamun')
                qty_list.append(int(food))
                amt_list.append(int(food)*149)
            st.write("-----------------------------------------------")
                      
            col4, col5, col6 = st.columns(3)
            
            col4.image('images/manchurian.jpg',width=200)
            col4.success("Manchurian")
            if col4.checkbox(label ='@ ₹199',key =4):
                col4.warning('Enter QTY. -')
                food = col4.number_input(label="Manchurian", min_value=1,key=14)
                food_list.append('Manchurian')
                qty_list.append(int(food))
                amt_list.append(int(food)*199)
                      
            col5.image('images/khaman.jpg',width=200)
            col5.success("Khaman")
            if col5.checkbox('₹99',key =5):
                col5.warning('Enter QTY. -')
                food = col5.number_input(label="khaman", min_value=1,key=15)
                
                food_list.append('Khaman')
                qty_list.append(int(food))
                amt_list.append(int(food)*99)             
                       
            col6.image('images/paneerbutter.jpg',width=200)
            col6.success("Paneer Butter")
            if col6.checkbox('@ ₹149',key =6):
                col6.warning('Enter QTY. -')
                food = col6.number_input(label="paneer butter", min_value=1,key=16)
                food_list.append('Paneer Butter')
                qty_list.append(int(food))
                amt_list.append(int(food)*149)
            st.write("-----------------------------------------------")
                
            col7, col8, col9 = st.columns(3)
            
            col7.image('images/pizza.jpg',width=200)
            col7.success("Pizza 🍕")
            if col7.checkbox(label ='@ ₹199',key =7):
                col7.warning('Enter QTY. -')
                food = col7.number_input(label="Pizza", min_value=1,key=17)
                food_list.append('pizza')
                qty_list.append(int(food))
                amt_list.append(int(food)*199)
                      
            col8.image('images/burger.jpg',width=200)
            col8.success("Burger 🍔")
            if col8.checkbox('@ ₹99',key =8):
                col8.warning('Enter QTY. -')
                food = col5.number_input(label="Burger", min_value=1,key=18)
                
                food_list.append('Burger')
                qty_list.append(int(food))
                amt_list.append(int(food)*99)             
                       
            col9.image('images/noodles.jpg',width=200)
            col9.success("Noodles 🍜")
            if col9.checkbox('@ ₹149',key =9):
                col9.warning('Enter QTY. -')
                food = col9.number_input(label="Noodles", min_value=1,key=19)
                food_list.append('Noodles')
                qty_list.append(int(food))
                amt_list.append(int(food)*149)
                
            with cart:
                hide_table_row_index = """
                <style>
                thead tr th:first-child {display:none}
                tbody th {display:none}
                </style>
                 """
                st.markdown(hide_table_row_index, unsafe_allow_html=True)
                
                order = {
                        'Food Name':food_list,
                        'Qty' : qty_list,
                        'Amount':amt_list
                    }
                
          
                cart = pd.DataFrame(order)
                cart_final = cart.dropna()
                cart_final['Qty'].astype(int)
                st.table(cart_final)
                total_amt = [ amt for amt in amt_list if amt!=None]
                total_item = [food for food in food_list if food !=None]
                total_qty = [qty for qty in qty_list if qty!=None]
                total_sum = sum(total_amt)
                st.subheader("Your Total Amout to be paid" + ' --  Rs.'+ str(total_sum) )
                
                payment = st.selectbox('How would you like to Pay',('Cash','UPI', 'Net Banking', 'Credit Card', 'Debit Card'))
                
                st.button ("Order Now", on_click=order_pressed, args= (st.session_state['details'][0], total_sum, payment ,total_item, total_qty))
            
            with myaccount:
                st.header('Update your details here')
                st.subheader("Enter updated email")
                up_email = st.text_input(label="mail",key=33, value = str(st.session_state['details'][4]))
                st.subheader("Enter updated name")
                up_name = st.text_input(label="name",key=34, value=str(st.session_state['details'][1]))
                st.subheader("Enter updated address")
                up_address = st.text_input(label="address",key=35, value=str(st.session_state['details'][2]))
                st.subheader("Enter updated phone number")
                up_number = st.text_input(label="phnumber",key=36, value=str(st.session_state['details'][3]))
                
                st.button('Update User Details', on_click = update_user_details , args=(st.session_state['details'][0], up_email, up_name, up_address, up_number))

                if st.checkbox("Do you want to change the password ?"):
                    st.subheader('Write Updated Password :')
                    up_passw =st.text_input (label="password",value="",placeholder="Enter updated password", type="password", key = 256)
                    up_conf_passw = st.text_input (label="conf_password", value="",placeholder="Enter updated password", type="password", key =257)
                    if up_passw == up_conf_passw:
                        st.button('Update Password', on_click=update_user_password, args=(st.session_state['details'][0], up_passw))
                    else :
                        st.info('Password does not match ')
                        
                if st.checkbox("Do you want to Delete your account ? "):
                    st.subheader("Are you sure you want to delete your account ?")
                    st.text(st.session_state['details'][0])
                    st.button('DELETE MY ACCOUNT', on_click = delete_user_show, args =(st.session_state['details'][0],))
                   
def delete_user_show(urd_id):
    delete_user(urd_id)
    LoggedOut_Clicked()
    st.success("Account Deleted Successfuly")

def LoggedOut_Clicked():
    st.session_state['loggedIn'] = False
    st.session_state['details'] = None
    st.session_state['checkout'] = False

def user_data_table():
    df = pd.DataFrame(get_user_data())
    return df


def admin_main_page():
    st.header('Admin Panel ')
        
    user, orders = st.tabs(['Users', 'orders' ])
        
    with user:
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            thead tr th: {display:none}
            </style> """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        st.subheader('user data display')
        s = user_data_table()
        st.table(s)
                
            
    with orders:
        st.subheader('order data display')
        hide_table_row_index = """
            <style>
            thead tr th:first-child {display:none}
            tbody th {display:none}
            thead tr th: {display:none}
            </style> """
        st.markdown(hide_table_row_index, unsafe_allow_html=True)
        order_df = pd.DataFrame(get_order_data())
        st.table(order_df)    
        st.subheader('Select the order id you want to get information of')
        ode_id = st.number_input(label="ord_id", min_value=1 )
        orderitem_pd = pd.DataFrame(get_orderitem_detail(ode_id))
        st.table(orderitem_pd)

def show_logout_page():
    loginSection.empty();
    with logOutSection:
        st.button ("Log Out", key="logout", on_click=LoggedOut_Clicked)
        

def LoggedIn_Clicked(email_id, password):
    if login(email_id, password):
        st.session_state['loggedIn'] = True
        st.session_state['details'] = get_details(email_id)
    else:
        st.session_state['loggedIn'] = False;
        st.session_state['details'] = None
        st.error("Invalid user name or password")
        
def signup_clicked(email, name, address ,phnumber,sign_password):
    try :
        if signup(email, name, address ,phnumber,sign_password):
            st.success("Signup successful ")
            st.balloons()
    except:
        st.warning('Invalid User ID or user ID already taken')
    
        
def show_login_page():
    with loginSection: 
        if st.session_state['loggedIn'] == False:
            
            login, signup,admin = st.tabs(["Login ✨", "Signup ❤️","admin"])
            with login:
                st.subheader('Login Here 🎉')         
                email_id = st.text_input (label="mail", placeholder="Enter your Email")
                password = st.text_input (label="pass",placeholder="Enter password", type="password")
                st.button ("Login", on_click=LoggedIn_Clicked, args= (email_id, password))
                   
                
            with signup:
                st.subheader('Signup 🫶')
                
                email = st.text_input(label="Email", value="", placeholder = "Enter your Email-ID", key = 10)
                if email == '':
                    st.warning('Enter your Email')
                elif len(email)<6:
                    st.warning('Email should be atleast 6 characters')

                name = st.text_input (label="Name", value="", placeholder="Enter your Name", key =9)
                if name == '':
                    st.warning('Enter your name')
                elif len(email)<=3:
                    st.warning('Name should be atleast 3 characters')
                
                address = st.text_input(label="Address", value="", placeholder ="Enter your Address:", key = 13)
                if address == '':
                    st.warning('Enter your Address')
                elif len(address)<=9:
                    st.warning('Address should be atleast 9 characters')
                    
                phnumber = st.text_input(label= "Mobile number", value="+91 ", placeholder ='Enter you Phone Number', key =14)
                if phnumber == '':
                    st.warning('Enter your Mobile Number')
                elif len(phnumber)<=9:
                    st.warning('Mobile Number should be atleast 10 digits')
                
                sign_password =  st.text_input (label="Password", value="",placeholder="Enter password", type="password", key = 11)
                if sign_password == '':
                    st.warning('Enter Password')
                elif len(sign_password)< 3:
                    st.warning('Password should be atleast 3 characters')
                cnf_password =  st.text_input (label="Confirm Password", value="",placeholder="confirm your password", type="password", key = 12)
                if sign_password != cnf_password:
                    st.warning('Password does not match')
                agree = st.checkbox('I agree to the terms and conditions')
                
                if not agree:
                    st.warning('You must agree to the terms and conditions')
                    
                if len(email) > 4 and len(phnumber)>10 and  len(address)>3 and agree :
                    if st.button('Register now',on_click=signup_clicked, args= (email, name, address ,phnumber,sign_password)):
                        st.write("Successfully Registered")
                else:
                    st.warning("Please Fill all the Details")
           
            with admin:
                admin_name=st.text_input("Enter Admin Username")
                admin_password=st.text_input("Enter Admin Password")
                if st.button('Login Now'):
                    if admin_name=="admin" and admin_password=="333":
                        admin_main_page()
                    else:
                        st.warning("Wrong ID & Paasword")
with headerSection:
    st.title("Online Food Ordering System 😋")
    if 'loggedIn' not in st.session_state:
        st.session_state['loggedIn'] = False
        show_login_page() 
    if 'checkout' not in st.session_state:
        st.session_state['checkout'] = False
    else:
        if st.session_state['loggedIn']:
            show_logout_page()    
            show_main_page()
        elif st.session_state['checkout']:
            show_logout_page()
            show_checkout_page()
        else:
            show_login_page()

            
hide_st_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            header {visibility: hidden;}
            </style>
            """
st.markdown(hide_st_style, unsafe_allow_html=True)
