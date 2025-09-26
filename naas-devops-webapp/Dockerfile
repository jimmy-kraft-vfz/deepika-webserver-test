# Use official Nginx image
FROM nginx:alpine

# Create html directory (if it doesn’t exist)
RUN mkdir -p /usr/share/nginx/html

# Remove any default content
RUN rm -rf /usr/share/nginx/html/*

# Copy your webpage into container
COPY app/ /usr/share/nginx/html/

# Expose port 80
EXPOSE 80

# Start Nginx
CMD ["nginx", "-g", "daemon off;"]
