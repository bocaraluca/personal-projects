import React, { useState } from "react";
import { Box, Button, Paper, TextField, Typography } from "@mui/material";
import LoginIcon from "@mui/icons-material/Login";
import { deepPurple, purple } from "@mui/material/colors";
import { useNavigate } from "react-router-dom";

const LoginForm = () => {
  const [nume, setNume] = useState("");
  const [parola, setParola] = useState("");
  const [clicked, setClicked] = useState(false);
  const navigate = useNavigate();

  const handleSubmit = (e) => {
    e.preventDefault();
    if (nume === "elev" && parola === "elev") {
      let path = "/Books";
      navigate(path);
    } else {
      setClicked(true);
    }
  };

  return (
    <Box
      component="form"
      onSubmit={handleSubmit}
      sx={{
        width: "450px",
        minHeight: "280px",
        margin: "50px auto",
      }}
    >
      <Paper
        elevation={4}
        sx={{
          width: "450px",
          minHeight: "280px",
          display: "flex",
          flexDirection: "column",
          alignItems: "center",
          justifyContent: "space-between",
          padding: 1,
          bgcolor: deepPurple[50],
          opacity: 0.9,
        }}
      >
        <Typography variant="h4" color={purple[800]}>
          Autentificare
          <LoginIcon fontSize="medium" />
        </Typography>
        <TextField
          required
          fullWidth
          variant="outlined"
          label="Nume utilizator:"
          name="nume"
          value={nume}
          error={clicked && nume !== "elev"}
          helperText={clicked && nume !== "elev" && "Nume sau parola incorecte"}
          onChange={(e) => {
            setNume(e.target.value);
            setClicked(false);
          }}
        />
        <TextField
          required
          type="password"
          fullWidth
          label="Parolă:"
          variant="outlined"
          name="parola"
          value={parola}
          error={clicked && parola !== "elev"}
          helperText={clicked && parola !== "elev" && "Nume utilizator sau parolă incorecte!"}
          onChange={(e) => {
            setParola(e.target.value);
            setClicked(false);
          }}
        />
        <Button fullWidth type="submit" variant="contained" sx={{ bgcolor: purple[800] }}>
          Autentificare
        </Button>
      </Paper>
    </Box>
  );
};

export default LoginForm;