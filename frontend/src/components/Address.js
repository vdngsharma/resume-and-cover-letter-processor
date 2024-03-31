import React from 'react';

const Address = ({value, onChange}) => {
    return (
        <label>
          Address:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default Address;