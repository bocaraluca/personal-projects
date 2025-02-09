import * as React from 'react';
import Radio from '@mui/material/Radio';
import FormControlLabel from '@mui/material/FormControlLabel';
import FormControl from '@mui/material/FormControl';
import FormLabel from '@mui/material/FormLabel';
import { TextField } from '@mui/material';
import { SettingsVoice } from '@mui/icons-material';

export default function IntrebareUnic({intrebare}) {

  return (
    <FormControl sx={{border: 1, padding: 3, borderRadius: 3}}>
      <FormLabel>{intrebare}</FormLabel>
      <TextField>
      </TextField>
    </FormControl>
  );
}