def get(): return'''

<html>
    <head>
        <style>
            div.box{
            
            /* sets border and spacing*/
            border: 2px solid black;
            background: white;
            padding-top: 7em;
            padding-left: 1em;
            padding-right: 1em;
            padding-bottom: 1em;

            /* centers the box*/
            position: absolute;
            top: 0;
            bottom: 0;
            left: 0;
            right: 0;
            margin: auto;

            /*set size of box*/
            width: 30vw;
            height: 50vh;

            overflow: auto;
            
            z-index: 10;

            box-shadow: 1em 1em 0.5em rgba(0,0,0,0.5);

            margin-top: 3em;
            }

            .title{
                font-weight: bold;
                font-size: 2em;
                text-align: center;
                margin-bottom: 1em;
                background: #00cccc;
                color: white;
                padding: 1em;
            }

            .inprompt{
                font-size: 1.25em;
                padding-bottom: 1.5em;
                text-align: center;
            }

            div.button{
                border: 3px outset;
                margin-top; 2em;
                margin-left: 3em;
                margin-right: 3em;
                padding: 1em;
                background: #00415a;
                text-align: center;
                font-weight: bold;
                font-size: 1.5em;
                color: white;

                
            
            }
                
            
            
            
        </style>
    </head>
    <body>
        <div class="box">
        
            <div class="inprompt" >Email: &emsp;<input size=20></div>
            <div class="inprompt">Full Name:&emsp;<input size=20></div>
            <div class="inprompt">Date of Birth:&emsp;<input type="date"></div>
            <div class="inprompt">Password:&emsp;<input type="password" size=20></div>
            <div class="button">Sign Up</div>

        
        
        </div>
        
            
    </body>
</html>

'''