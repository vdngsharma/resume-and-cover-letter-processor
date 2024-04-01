import React from 'react';

const Duties = ({value, onChange}) => {
    return (
      <label className='label'>
          DUTIES
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default Duties;
