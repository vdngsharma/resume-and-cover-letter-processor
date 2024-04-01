import React from 'react';
import './styles.css';

const Address = ({value, onChange}) => {
    return (
      <label className='label'>
          ADDRESS
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default Address;