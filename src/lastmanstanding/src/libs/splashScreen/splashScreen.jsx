import React from 'react';
import './splashScreen.css';
import LMSLogo from '../../images/LMS2.gif';

const SplashScreen = () => {
  return (
    <div className='splashScreen' style={{background: '#ffffff'}}>
      <img
        src={LMSLogo}
        className='splashScreenImage'
      />
    </div>
  );
};

export default SplashScreen;
