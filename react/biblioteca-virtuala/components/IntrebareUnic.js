import * as React from 'react';
import Radio from '@mui/material/Radio';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';

export default function IntrebareUnic({intrebare, r1, r2, r3, r4}) {
  return (
    <FormControl sx={{border: 1, padding: 3, borderRadius: 3}}>
      <FormLabel id="demo-radio-buttons-group-label">{intrebare}</FormLabel>
      <RadioGroup
        aria-labelledby="demo-radio-buttons-group-label"
        defaultValue="female"
        name="radio-buttons-group"
      >
        <FormControlLabel value={r1} control={<Radio />} label={r1} />
        <FormControlLabel value={r2} control={<Radio />} label={r2} />
        <FormControlLabel value={r3} control={<Radio />} label={r3} />
        <FormControlLabel value={r4} control={<Radio />} label={r4} />
      </RadioGroup>
    </FormControl>
  );
}