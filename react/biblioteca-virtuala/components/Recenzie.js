import * as React from 'react';
import Rating from '@mui/material/Rating';
import Box from '@mui/material/Box';
import StarIcon from '@mui/icons-material/Star';
import { Alert } from '@mui/material';
import CheckIcon from '@mui/icons-material/Check';

const labels = {
  1: 'Dezamăgitor',
  2: 'Acceptabil',
  3: 'Bun',
  4: 'Foarte bun',
  5: 'Excelent',
};

function getLabelText(value) {
  return `${value} Star${value !== 1 ? 's' : ''}, ${labels[value]}`;
}

export default function Recenzie() {
  const [value, setValue] = React.useState(0);
  const [hover, setHover] = React.useState(-1);
  const [alertOpen, setAlertOpen] = React.useState(false);

  const handleRatingChange = (e, newValue) => {
    setValue(newValue);
    setAlertOpen(true);
  };


  return (
    <Box sx={{
      display: 'flex',
      flexDirection: 'column',
      alignItems: 'center',
      paddingTop: '20px',
      paddingBottom: '40px'
    }}>
      {alertOpen && value &&
        <Alert icon={<CheckIcon fontSize="inherit" />} severity="success">
        Recenzia a fost înregistrată cu succes! Ai acordat {value} stele.
        </Alert>
      }
    <Box
      sx={{
        width: 200,
        display: 'flex',
        alignItems: 'center',
        justifyContent: 'center'
      }}
    >
      
      <Rating
        name="hover-feedback"
        value={value}
        precision={1}
        getLabelText={getLabelText}
        onChange={handleRatingChange}
        onChangeActive={(event, newHover) => {
          setHover(newHover);
        }}
        emptyIcon={<StarIcon style={{ opacity: 0.55 }} fontSize="inherit" />}
      />
      {value !== null && (
        <Box sx={{ ml: 2 }}>{labels[hover !== -1 ? hover : value]}</Box>
      )}
      </Box>
    </Box>
  );
}