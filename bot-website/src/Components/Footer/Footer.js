import React from 'react'
import './Footer.css'
import { BsFacebook,BsTelegram } from 'react-icons/bs';

const Footer = () => {
  return (
        <section  id="footer">
            <div className="footerCent">
                <ul className='footlinks'>
                    <li>About</li>
                    <li>Policy</li>
                    <li>Terms</li>
                </ul>
                <div className="logo">
                    <h2>The Mind Buddy</h2>
                </div>
                
                <ul className="contactsites">
                    <li>Contact</li>
                    <li><BsFacebook fontSize={'1.5rem'}/></li>
                    <li><BsTelegram fontSize={'1.5rem'}/></li>
                </ul>
                
            </div>
        </section>
  )
}

export default Footer