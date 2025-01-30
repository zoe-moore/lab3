

function check(){

    console.log("test");
    let email = document.getElementById("email").value;
    let name = document.getElementById("name").value;
    let bday = document.getElementById("bday").value;
    let password = document.getElementById("password").value;
    let at_count=0;
    let bday_obj = new Date(bday);
    let banner = document.createElement("div");
    document.body.appendChild(banner);

    for(let i=0;i<email.length;i++)
        {
            if (email[i]=='@')
              {  at_count++;  } 
        }
    
    
    if (email=="" || name=="" || bday==""|| password=="")
    {
        banner.classList.add("error");
        banner.appendChild(document.createTextNode("One or more fields left blank."));
    }

    else if (at_count!=1 || email[0]=='@' || email[email.length-1]=='@')
    {
         //alert("Invalid Email Address");S
         banner.classList.add("error");
         banner.appendChild(document.createTextNode("Invalid Email Address"));
    }

    else if(bday_obj.getTime()>(Date.now()-13*365.25*24*60*60*1000))
    {
        banner.classList.add("error");
        banner.appendChild(document.createTextNode("Invalid Birthdate"));
    }

    else
    {
        banner.classList.add("welcome");
        banner.appendChild(document.createTextNode("Welcome"));

    }


}