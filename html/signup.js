

function check(){

    console.log("test");
    let email = document.getElementById("email").value;
    let name = document.getElementById("name").value;
    let bday = document.getElementById("bday").value;
    let password = document.getElementById("password").value;
    let at_count=0;
    let bday_obj = new Date(bday);
    let bday_mil;
    
    if (email=="" || name=="" || bday==""|| password=="")
    {
        alert("One or more fields left blank.");  
    }

    for(let i=0;i<email.length;i++)
    {
        if (email[i]=='@')
          {  at_count++;  } 
    }

    if (at_count!=1 || email[0]=='@' || email[email.length-1]=='@')
        {alert("Invalid Email Address");}

    if(bday_obj.getTime()>(Date.now()-13*365.25*24*60*60*1000))
    {
        alert("Invalid Birthdate");
    }


}