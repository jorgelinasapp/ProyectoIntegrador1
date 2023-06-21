CREATE DATABASE proyectoFinal;
USE proyectoFinal;
CREATE TABLE `Normativa`(
    `id_Normativa` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `NroNormativa` INT NOT NULL,
    `id_TipoNormativa` INT NOT NULL,
    `Fecha` DATE NOT NULL,
    `Descripcion` VARCHAR(450) NOT NULL,
    `id_Categoria` INT NOT NULL,
    `id_Jurisdiccion` INT NOT NULL,
    `id_OrganoLegislativo` INT NOT NULL,
    `PalabrasClave` VARCHAR(255) NOT NULL
);
CREATE TABLE `Jurisdiccion`(
    `id_Jurisdiccion` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `Jurisdiccion` VARCHAR(255) NOT NULL
);
CREATE TABLE `Categoria`(
    `id_Categoria` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `TipoCategoria` VARCHAR(255) NOT NULL
);
CREATE TABLE `OrganoLegislativo`(
    `id_OrganoLegislativo` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `OrganoLegislativo` VARCHAR(255) NOT NULL
);
CREATE TABLE `TipoNormativa`(
    `id_TipoNormativa` INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY,
    `TipoNormativa` VARCHAR(255) NOT NULL
);
ALTER TABLE
    `Normativa` ADD CONSTRAINT `normativa_id_tiponormativa_foreign` FOREIGN KEY(`id_TipoNormativa`) REFERENCES `TipoNormativa`(`id_TipoNormativa`);
ALTER TABLE
    `Normativa` ADD CONSTRAINT `normativa_id_organolegislativo_foreign` FOREIGN KEY(`id_OrganoLegislativo`) REFERENCES `OrganoLegislativo`(`id_OrganoLegislativo`);
ALTER TABLE
    `Normativa` ADD CONSTRAINT `normativa_id_jurisdiccion_foreign` FOREIGN KEY(`id_Jurisdiccion`) REFERENCES `Jurisdiccion`(`id_Jurisdiccion`);
ALTER TABLE
    `Normativa` ADD CONSTRAINT `normativa_id_categoria_foreign` FOREIGN KEY(`id_Categoria`) REFERENCES `Categoria`(`id_Categoria`);
