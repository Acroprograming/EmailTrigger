from django.shortcuts import render
from django.core.mail import EmailMultiAlternatives

#method index
def index(request):
    #if method used is post
    if request.method == 'POST':
        #initialise subject senderEmail and recieving email
        subject, from_email, to = 'Feedback Ticket #Number ', 'acronptel@gmail.com', 'premindian288@gmail.com'
        #get ticket number
        num=request.POST.get('5b46029bc20a6b25bbf51e76')
        #get feedback
        feedback=request.POST.get('5b471e70c20a6b5d789f560d')
        #get user name
        user=request.POST.get('5b46029bc20a6b25bbf51e74')
        #replace value of #Number in the subject
        subject=subject.replace("#Number",num)
        #initialise html message
        data="<p>Hello <span class='atwho-inserted' data-atwho-at-query='#'><span id='5b46029bc20a6b25bbf51e74' class='customFields'>#single line text</span></span>⁠,</p><p><br></p><p>Greetings from hubbler. It has been privilege to serve you.&nbsp;</p><p>Your below Feedback &nbsp;is received:</p><p><span class='atwho-inserted' data-atwho-at-query='#'><span id='5b471e70c20a6b5d789f560d' class='customFields'>#Paragraph</span></span>⁠&nbsp;</p><p><br></p><p>Your Ticket Number : <span class='atwho-inserted' data-atwho-at-query='#'><span id='5b46029bc20a6b25bbf51e76' class='customFields'>#Number</span></span>⁠ is raised and will be responded to asap.</p><p><br></p><p>Happy Hubblering!!</p><p>Team Hubbler</p>"
        #replace value of #Paragraph in data
        data=data.replace("#Paragraph",feedback)
        #replace value of #Number in data
        data=data.replace("#Number",num)
        #replace value of #single line text in data
        data=data.replace("#single line text",user)
        #add some text content
        text_content = 'Feed back recieved'
        #initialise email message
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        #attach html data
        msg.attach_alternative(data, "text/html")
        #send
        msg.send()
    context = { 
        "fields" :
        [
            {  
                'type': 'single line text',
                '_id':   '5b46029bc20a6b25bbf51e74',
                'lbl':   'single line text',
                "placeholder": "User name"
            },
            { 
                'type': 'paragraph', 
                '_id':   '5b471e70c20a6b5d789f560d', 
                'lbl':    'paragraph',
                "placeholder": "Feedback"
            },
            { 
                'type': 'number', 
                '_id': '5b46029bc20a6b25bbf51e76',
                'lbl': 'Number',
                "placeholder": "Ticket number"
            }
        ],
    }

    return render(request,'interview/index.html',context)

    

