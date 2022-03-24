import React from 'react'
import './Features.css'

import { SiChatbot } from 'react-icons/si';
import { BsFillPeopleFill } from 'react-icons/bs';


const Features = () => {
  return (
    <div className="features">
        <div className="featureCent">
           <div className="feature diffstyle1">
               <h1>More than just a chat bot</h1>
               <p>
                   With human support technology,we can just text normally with fastest data processing, and you don't even realize that you talking to a bot
               </p>
           </div>
           
           <div className="feature diffstyle2">
                   <h2>Humanizing Bot</h2>
                   <p>We push our bot limit to understand the way people chat as they normally do in daily basis</p>
                   <SiChatbot color='white' fontSize='1.5em' />
                   {/* will add icons here  */}
           </div>
           <div className="feature diffstyle2">
               {/* will add icons here */}
               <h3>Bot Empathy</h3>
               <p>We try to understand a person's mental health problems and condition through text</p>
               <BsFillPeopleFill color='white'
               fontSize={'1.5em'}/>
           </div>
           
        </div>
    </div>
  )
}

export default Features