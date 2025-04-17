from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from app1.models import Items,IceReviews,IceCreamImage,Customers, Stores, IceCertificate, card
from django.contrib import messages
from random import randint
import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

def cat(request):
    return render(request,'cat.html')

def __init__(request):
    cert=IceCertificate.objects.all()
    return render(request,"base.html",{'cerf':cert})

# def certificates_processor(request):
#     return {'cerf': IceCertificate.objects.all()}
# Create your views here.
def show(request):
    data=Items.objects.all()
    rating=IceReviews.objects.all()
    return render(request,"show.html",{'data':data})

def home(request):
    return render(request,'base.html')

def about(request):
     return render(request,'base.html') 
 
def other_stores(request):
    all_stores=Stores.objects.all()
    return render(request,'stores.html',{'stores':all_stores})
 

def rev(request):
    if request.method == "POST":
        order_id1 = request.POST.get("order_id")
        review_text = request.POST.get("review")
        rating = request.POST.get("rating")

        # Check if the customer exists
        check_customer = Customers.objects.filter(order_id=order_id1).first()
        
        # Check if the customer has already submitted a review
        check_customer_rev = IceReviews.objects.filter(order_id=order_id1).first()

        if check_customer and not check_customer_rev:
            ice_cream = check_customer.ice_name  
            IceReviews.objects.create(
                ice=ice_cream,
                user=check_customer, 
                order_id=order_id1, 
                rating=int(rating),
                review=review_text
            )
            messages.success(request, "Your review has been submitted successfully!")  # Success Message
        elif check_customer and check_customer_rev:
            messages.warning(request, "You have already submitted a review for this order.")  # Duplicate Review Message
        else:
            messages.error(request, "Invalid Order ID. Please check and try again.")  # Error Message

        return redirect('rev')  # Redirect to prevent form resubmission

    return render(request, 'rev.html')

def send_verification_email(email, random_number,bill, address, ice, q):
        # Use environment variables for sensitive data
        EMAIL_ADDRESS = os.getenv('EMAIL_ADDRESS', 'waseemhanif0018@gmail.com')
        EMAIL_PASSWORD = os.getenv('EMAIL_PASSWORD', 'puxn whgj igvv skus')  # App password or OAuth token
        SMTP_SERVER = 'smtp.gmail.com'
        SMTP_PORT = 587

        subject = 'Your Order Information'
        body = f'''
        <html>
            <body style="background-color: #f4f4f4; padding: 40px; text-align: center; font-family: Arial, sans-serif;">
                <div style="background-color: white; padding: 30px; border-radius: 10px; 
                            box-shadow: 0px 4px 15px rgba(0,0,0,0.1); display: inline-block; max-width: 400px;">
                    
                    <h2 style="color: #333; margin-bottom: 10px;">🎉 Order Confirmation</h2>
                    
                    <p style="font-size: 18px; color: #555; margin: 10px 0;">
                        Your Order ID:  
                        <strong style="font-size: 24px; color: #d9534f;">{random_number}</strong>
                    </p>

                    <hr style="border: none; height: 1px; background-color: #ddd; margin: 15px 0;">

                    <p style="font-size: 16px; color: #333; font-weight: bold; margin: 5px 0;">
                        Total Bill: <span style="color: #d9534f;">{bill} rupees</span>
                    </p>

                    <p style="font-size: 16px; color: #333; font-weight: bold; margin: 5px 0;">
                        Address: <a href="mailto:{address}" style="color: #007bff; text-decoration: none;">{address}</a>
                    </p>

                    <p style="font-size: 16px; color: #333; font-weight: bold; margin: 5px 0;">
                        Items Purchased: <span style="color: #28a745;">{q} {ice} Ice-Creem</span>
                    </p>

                    <hr style="border: none; height: 1px; background-color: #ddd; margin: 15px 0;">

                    <p style="font-size: 14px; color: #888;">Thank you for shopping with us! 🎈</p>
                </div>
            </body>
        </html>
        '''

        # Create the email
        msg = MIMEMultipart()  # Corrected
        msg['Subject'] = subject
        msg['From'] = EMAIL_ADDRESS
        msg['To'] = email  # Sending to only one recipient
        msg.attach(MIMEText(body, 'html'))  # Use 'html' instead of 'plain' for formatting

        try:
            # Send the email
            with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
                server.starttls()  # Upgrade the connection to a secure encrypted SSL/TLS connection
                server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)  # Log in to the email server
                server.sendmail(EMAIL_ADDRESS, email, msg.as_string())  # Send the email
                print('Email sent successfully!')
        except Exception as e:
            print(f'Error: {e}') 
            
def card1(cvc, cardno, nameoncard):
    check = card.objects.filter(cardno=cardno, cvc=cvc, nameoncard=nameoncard).first()
    # rs=check.amount
    if check:
        print("Card Exist")
        return True
    else:
        print("Please Enter Valid Card")
        return False

    
def buy(request, ice_id):
    ice = get_object_or_404(Items, pk=ice_id)

    if request.method == "POST":
        name = request.POST.get("name")
        address = request.POST.get("address")
        email_from_form = request.POST.get("email")
        q = request.POST.get("q")
        phone = request.POST.get("phone")
        cardno = request.POST.get("cardno")
        nameoncard = request.POST.get("nameoncard")
        cvc = request.POST.get("cvc")
        q1 = int(q)

        if not card1(cvc, cardno, nameoncard):
            messages.error(request, "Please Enter valid card details.")
            # return redirect('ice_dec', ice_id=ice.id)
        else:

            # Generate unique order ID
            while True:
                random_number = randint(10000, 99999)
                if not Customers.objects.filter(order_id=random_number).exists():
                    break

            if ice.avalible_ch >= q1:
                ice.avalible_ch -= q1
                ice.save()
                
                bill = ice.price * q1
                check = card.objects.filter(cardno=cardno, cvc=cvc, nameoncard=nameoncard).first()
                
                if check.amount >= bill:
                        check.amount -= bill
                        check.save()

                        customer = Customers(
                            name=name,
                            phone=phone,
                            address=address,
                            email=email_from_form,
                            ice_name=ice,
                            order_id=random_number,
                            bill=bill
                        )
                        customer.save()

                        send_verification_email(email_from_form, random_number, bill, address, ice, q)
                        
                        messages.success(request, f"Success! Your Order ID is {random_number}, Your Bill is {bill} Rupees")
                else:
                    messages.error(request, f"Not enough Blunce. In Your Card, Your Crent Blance is {check.amount}RS")
                    
            else:
                messages.error(request, f"Not enough stock. Available Ice Creams: {ice.avalible_ch}")
                return redirect('ice_dec', ice_id=ice.id)

    return redirect('ice_dec', ice_id=ice.id)


def ice_dec(request, ice_id):
    """Handles ice cream details and buying process"""
    ice = get_object_or_404(Items, pk=ice_id)  # Fetch ice cream object
    ice_review = IceReviews.objects.filter(ice=ice)
    ice_images = IceCreamImage.objects.filter(person=ice)

    # Fix: Use the correct variable name (ice_review)
    ratings = [review.rating for review in ice_review]
    if ratings:
        avg_rating = sum(ratings) / len(ratings)
    else:
        avg_rating = 0  # Handle case with no ratings

    context = {
        'ice': ice,
        'ice_rev': ice_review,
        'ice_image': ice_images,
        'avg_rating': round(avg_rating, 1),  # Rounded to 1 decimal place
    }

    return render(request, 'ice_dec.html', context)



    # return render(request, 'ice_dec.html', {'ice': ice, 'ice_rev': ice_review, 'ice_image': ice_images})
