import * as React from 'react';
import RadioGroup from '@mui/material/RadioGroup';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import { Checkbox } from '@mui/material';

export default function IntrebareMultiple({intrebare, r1, r2, r3, r4}) {
  return (
    <FormControl sx={{border: 1, padding: 3, borderRadius: 3}}>
      <FormLabel>{intrebare}</FormLabel>
        <FormControlLabel value={r1} control={<Checkbox />} label={r1} />
        <FormControlLabel value={r2} control={<Checkbox />} label={r2} />
        <FormControlLabel value={r3} control={<Checkbox />} label={r3} />
        <FormControlLabel value={r4} control={<Checkbox />} label={r4} />
    </FormControl>
  );
}