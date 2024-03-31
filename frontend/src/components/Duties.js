import React from 'react';

const Duties = ({value, onChange}) => {
    return (
        <label>
          Duties:
          <input
          type = "text"
          value = {value}
          onChange = {onChange}
          />
        </label>
    );
};

export default Duties;
