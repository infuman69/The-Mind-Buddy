import React from "react";
import bot2 from "../../assets/bot2.png";
import "./Bot.css";
import telegram from "../../assets/telegram.png";
const Bot = () => {
  return (
    <section id="bot">
      <div className="container-bot">
        <div className="bot-left">
          <img src={bot2} className="bot-logo" alt="bot" />
        </div>
        {/* <div className="link-txt">
          <span>Let's talk to a bot!!</span>
        </div>
        <div className="link">
          <img src={telegram} className="tel" />
          <button className="linkb">https://t.me/TheMindBuddyBot </button>
        </div> */}
      </div>
    </section>
  );
};
export default Bot;
