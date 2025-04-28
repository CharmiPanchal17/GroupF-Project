module.exports = {
    transform: {
      "^.+\\.(js|jsx|ts|tsx)$": "babel-jest", // Use Babel to transform modern JavaScript
    },
    transformIgnorePatterns: [
      "node_modules/(?!axios|react-hot-toast)", // Transform ESM modules like axios and react-hot-toast
    ],
    moduleNameMapper: {
      "\\.(css|less|scss|sass)$": "identity-obj-proxy", // Mock CSS imports
    },
    testEnvironment: "jsdom", // Use jsdom for testing React components
  };