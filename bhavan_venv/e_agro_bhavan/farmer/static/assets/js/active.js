function activateButton(buttonId) {
    const buttons = document.querySelectorAll('.btn');
    
    buttons.forEach(button => {
      if (button.id === buttonId) {
        button.classList.add('active');
      } else {
        button.classList.remove('active');
      }
    });
  }