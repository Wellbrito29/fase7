-- ---
-- Globals
-- ---

-- SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
-- SET FOREIGN_KEY_CHECKS=0;

-- ---
-- Table 'Sensores'
-- 
-- ---

DROP TABLE IF EXISTS `Sensores`;
		
CREATE TABLE `Sensores` (
  `id_sensor` INTEGER NOT NULL AUTO_INCREMENT,
  `sensor_tipo` VARCHAR(50) NOT NULL,
  `sensor_local` VARCHAR(100) NOT NULL,
  `id_planta` INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_sensor`)
);

-- ---
-- Table 'Plantacao'
-- 
-- ---

DROP TABLE IF EXISTS `Plantacao`;
		
CREATE TABLE `Plantacao` (
  `id_planta` INTEGER NOT NULL AUTO_INCREMENT,
  `cultura` VARCHAR(50) NOT NULL,
  `area_planta` DECIMAL(10,2) NOT NULL,
  `local_planta` VARCHAR(100) NOT NULL,
  PRIMARY KEY (`id_planta`)
);

-- ---
-- Table 'Dados_do_sensor'
-- 
-- ---

DROP TABLE IF EXISTS `Dados_do_sensor`;
		
CREATE TABLE `Dados_do_sensor` (
  `id_sens_dado` INTEGER NOT NULL AUTO_INCREMENT,
  `umidade` INTEGER NOT NULL,
  `ajuste_data` DATETIME NOT NULL,
  `ph_valor` DECIMAL(4,2) NOT NULL,
  `nutri_qntd` DECIMAL(5,2) NOT NULL,
  `dado_clima` VARCHAR(100) NOT NULL,
  `id_sensor` INTEGER NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id_sens_dado`)
);

-- ---
-- Foreign Keys 
-- ---

ALTER TABLE `Sensores` ADD FOREIGN KEY (id_planta) REFERENCES `Plantacao` (`id_planta`);
ALTER TABLE `Dados_do_sensor` ADD FOREIGN KEY (id_sensor) REFERENCES `Sensores` (`id_sensor`);

-- ---
-- Table Properties
-- ---

-- ALTER TABLE `Sensores` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Plantacao` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;
-- ALTER TABLE `Dados_do_sensor` ENGINE=InnoDB DEFAULT CHARSET=utf8 COLLATE=utf8_bin;

-- ---
-- Test Data
-- ---

-- INSERT INTO `Sensores` (`id_sensor`,`sensor_tipo`,`sensor_local`,`id_planta`) VALUES
-- ('','','','');
-- INSERT INTO `Plantacao` (`id_planta`,`cultura`,`area_planta`,`local_planta`) VALUES
-- ('','','','');
-- INSERT INTO `Dados_do_sensor` (`id_sens_dado`,`umidade`,`ajuste_data`,`ph_valor`,`nutri_qntd`,`dado_clima`,`id_sensor`) VALUES