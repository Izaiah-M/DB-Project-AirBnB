CREATE TABLE `users` (
  `id` int PRIMARY KEY,
  `name` text,
  `email` text,
  `created_at` text,
  `updated_at` text
);

CREATE TABLE `homes` (
  `id` int PRIMARY KEY,
  `address` text,
  `price_per_night` int,
  `created_at` text,
  `updated_at` text
);

CREATE TABLE `users_homes` (
  `id` int PRIMARY KEY,
  `user_id` int,
  `home_id` int,
  `reservations_id` int,
  `created_at` text,
  `updated_at` text
);

CREATE TABLE `reservations` (
  `id` int PRIMARY KEY,
  `role` ENUM ('owner', 'visitor'),
  `start_date` text,
  `end_date` text,
  `created_at` text,
  `updated_at` text
);

ALTER TABLE `users_homes` ADD FOREIGN KEY (`user_id`) REFERENCES `users` (`id`);

ALTER TABLE `users_homes` ADD FOREIGN KEY (`home_id`) REFERENCES `homes` (`id`);

ALTER TABLE `users_homes` ADD FOREIGN KEY (`reservations_id`) REFERENCES `reservations` (`id`);
