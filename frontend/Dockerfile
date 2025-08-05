FROM node:18-alpine

WORKDIR /app

COPY package*.json ./

# نصب پکیج های مورد نیاز
RUN npm install

# کپی کردن تمام فایل های پروژه
COPY . .

# build کردن پروژه Vue.js
# این دستور فایل های آماده را در پوشه dist ایجاد می کند
RUN npm run build

# نصب پکیج serve به صورت global برای اجرای فایل های build شده
# این پکیج یک وب سرور سبک است
RUN npm install -g serve

EXPOSE 8002

# دستور شروع برنامه
# serve -s dist به پکیج serve می گوید که فایل های استاتیک را از پوشه dist اجرا کند
CMD ["serve", "-s", "dist"]