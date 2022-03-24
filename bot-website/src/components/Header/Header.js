import React, { useEffect } from "react";
import "./Header.css";
import Button from "../UI/Button/Button";
import "../UI/Button/button.css";
import banner from "../../assets/banner.mp4";


const Header = () => {

  return (
    <section id="header">
      <div className="container header">
        <div className="header-left" >
          <h1>
            <span>Worlds first</span>
            <span>cross-platform secure</span>
            <span>messaging system</span>
          </h1>
          <p className="u-text-small">
            Mindbuddy is a platform which tries to resolve mental health issues
            by bots.bdjoewfbo ebfiwqbf e fwefewfniwoenfiownfionwoifnoinlkml mn
          </p>
          <div className="header-cta">
            <Button text={"Get Started"} className='btn' href={"#"} />
          </div>
        </div>
        <div className="header-right" >
          <video autoPlay loop muted className="video-banner">
            <source src={banner} type="video/mp4"></source>
          </video>
        </div>
      </div>
    </section>
  );
};

export default Header;
