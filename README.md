# Shoppit E-commerce API

Welcome to **Shoppit**, a modern e-commerce API built using Django Rest Framework (DRF). This API serves as the backend for an e-commerce platform, enabling essential functionalities like product listing, user authentication, cart management, order processing, and payment integration.

---

## 🚀 **Features**
- **User Authentication**: Register, login, and manage user accounts.
- **Product Management**: View product listings, categories, and detailed product information.
- **Cart Management**: Add, update, and remove items from the cart.
- **Payment Integration**: Supports payment gateways like PayPal and Flutterwave.

---

## 🛠️ **Technologies Used**
- **Backend**: Django Rest Framework (DRF)
- **Database**: SQlite3
- **Payment Gateways**: PayPal, Flutterwave
- **Deployment**: Deployed on Render (update as applicable)

---

## 📦 **Installation and Setup**

1. **Clone the repository:**
   ```bash
   git clone https://github.com/CodeWithClinton/shoppit-api
   cd shoppit-api
   ```

2. **Create a virtual environment and activate it:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up the environment variables:**
   Create a `.env` file in the root directory with the following variables:
   ```env
   SECRET_KEY=your_secret_key_here
   DEBUG=True  # Set to False in production
   DATABASE_URL=your_database_url_here
   PAYPAL_CLIENT_ID=your_paypal_client_id_here
   PAYPAL_SECRET=your_paypal_secret_here
   FLUTTERWAVE_PUBLIC_KEY=your_flutterwave_public_key_here
   FLUTTERWAVE_SECRET_KEY=your_flutterwave_secret_key_here
   ```

5. **Apply database migrations:**
   ```bash
   python manage.py migrate
   ```

6. **Run the development server:**
   ```bash
   python manage.py runserver 8001
   ```

The API will be accessible at [http://127.0.0.1:8001/](http://127.0.0.1:8001/).

---

## 📚 **API Endpoints**

| **Endpoint**                  | **Method** | **Description**                         |
|-------------------------------|------------|-----------------------------------------|
| `/products`                    | GET        | List all products                       |
| `/product_detail/<slug:slug>`  | GET        | Retrieve details of a specific product  |
| `/add_item/`                   | POST       | Add an item to the cart                 |
| `/product_in_cart`             | GET        | Check if a product is in the cart       |
| `/get_cart_stat`               | GET        | Get cart statistics (like total items)  |
| `/get_cart`                    | GET        | Retrieve the contents of the cart       |
| `/update_quantity/`            | PATCH      | Update the quantity of a cart item      |
| `/delete_cartitem/`            | DELETE     | Remove an item from the cart            |
| `/get_username`                | GET        | Retrieve the username of the logged-in user |
| `/user_info`                   | GET        | Retrieve the user’s information        |
| `/register_user/`              | POST       | Register a new user                     |
| `/initiate_payment/`           | POST       | Initiate a payment request              |
| `/payment_callback/`           | POST       | Handle the payment callback             |
| `/initiate_paypal_payment/`    | POST       | Initiate a PayPal payment request       |
| `/paypal_payment_callback/`    | POST       | Handle the PayPal payment callback      |



---


## 🛠️ **Deployment**
1. Set `DEBUG=False` in the `.env` file.
2. Configure `ALLOWED_HOSTS` in `settings.py` to include your domain name or server IP.
3. Use `gunicorn` and `nginx` for production deployment.

---

## 🤝 **Contributing**
We welcome contributions! To contribute:
1. Fork the repo.
2. Create a new feature branch: `git checkout -b feature/your-feature-name`
3. Commit your changes: `git commit -m 'Add a new feature'`
4. Push to the branch: `git push origin feature/your-feature-name`
5. Open a Pull Request.

---



Happy Coding! 🚀

