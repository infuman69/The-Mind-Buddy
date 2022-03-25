import React from "react";
import bot2 from "../../assets/bot2.png";
import "./Bot.css";
import {FaTelegram} from 'react-icons/fa';

const Bot = () => {
  const getBot=()=>{
    window.location.href = 'https://t.me/TheMindBuddyBot'; 
  }
  return (
    <section id="bot">
      <div className="container-bot">
        <div className="bot-left">
          <img src={bot2} className="bot-logo" alt="bot" />
        </div>
        <div className="link-txt">
          <span>Lets talk to a bot !</span>
        </div>
        <div className="link">
          <button className="linkb" onClick={getBot}>MindBuddyBot <FaTelegram/> </button>
        </div>
      </div>
    </section>
  );
};
export default Bot;
