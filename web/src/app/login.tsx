import React from 'react';
import './login.css';

const Login = () => {
  return (
    <div className='container'>
        <button className='button'>
            <img src="btn_google_signin_dark_normal_web@2x.png" alt="Google ログイン" />
        </button>
        <button className='discord-button button'><span className='discord-icon'>Discord</span></button>
    </div>
    
  );
}

export default Login;