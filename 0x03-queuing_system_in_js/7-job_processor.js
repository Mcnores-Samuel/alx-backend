#!/usr/bin/yarn dev
import { createQueue, Job } from 'kue';

const BLACKLISTED_NUMBERS = ['4153518780', '4153518781'];
const queue = createQueue();

/**
 * Sends a push notification to a user.
 * @param {String} phoneNumber
 * @param {String} message
 * @param {Job} job
 * @param {Function} done
 */
const sendNotification = (phoneNumber, message, job, done) => {
  const totalSteps = 2;
  let remainingSteps = totalSteps;
  const sendInterval = setInterval(() => {
    if (totalSteps - remainingSteps <= totalSteps / 2) {
      job.progress(totalSteps - remainingSteps, totalSteps);
    }
    if (BLACKLISTED_NUMBERS.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
      clearInterval(sendInterval);
      return;
    }
    if (remainingSteps === totalSteps) {
      console.log(
        `Sending notification to ${phoneNumber},`,
        `with message: ${message}`
      );
    }
    --remainingSteps || done();
    remainingSteps || clearInterval(sendInterval);
  }, 1000);
};

queue.process('push_notification_code_2', 2, (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
});
