const getGreetingMessage = () => {
    const hours = new Date().getHours();
  
    if (hours >= 5 && hours < 12) {
      return "صبح بخیر";
    } else if (hours >= 12 && hours < 17) {
      return "ظهر بخیر";
    } else if (hours >= 17 && hours < 20) {
      return "عصر بخیر";
    } else {
      return "شب بخیر";
    }
  };
  
  const greetingMessage = getGreetingMessage();
  