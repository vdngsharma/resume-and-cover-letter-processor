import React from 'react';

const Date = ({value, onChange}) => {
    return (
        <label className='label'>
          DATE
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default Date;
