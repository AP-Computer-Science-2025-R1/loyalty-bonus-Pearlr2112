forecast = int(input(" what is the forecast for tomorrow? :"))
rain = input(" is it going to rain tomorrow? yes or no :")
if rain == "no":
     if  forecast > 20:
        print("wear uniqo pants with your CTE High honor role shirt.")
elif 10 <= forecast < 20:
    print("wear uniqo pants with a a zip up hoodie.")
elif 5 <= forecast <10:
    print("wear your uniqo pants with your uniqo jacket.") 
else:
    print("Just stay inside and code python!")
if rain == "yes":
    if forecast > 20:
        print("wear uniqo pants and bring a umberlla.")
elif 10 <= forecast < 20:
    print("wear uniqo pants with a umberlla and a hoodie.")
elif 5 <= forecast < 10:
    print("wear uniqo pants with a big umbrella and a warm jacket.") 
else:
     print("Just stay inside and code python!")
