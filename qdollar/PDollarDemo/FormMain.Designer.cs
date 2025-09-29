namespace PDollarDemo
{
    partial class FormMain
    {
        /// <summary>
        /// Required designer variable.
        /// </summary>
        private System.ComponentModel.IContainer components = null;

        /// <summary>
        /// Clean up any resources being used.
        /// </summary>
        /// <param name="disposing">true if managed resources should be disposed; otherwise, false.</param>
        protected override void Dispose(bool disposing)
        {
            if (disposing && (components != null))
            {
                components.Dispose();
            }
            base.Dispose(disposing);
        }

        #region Windows Form Designer generated code

        /// <summary>
        /// Required method for Designer support - do not modify
        /// the contents of this method with the code editor.
        /// </summary>
        private void InitializeComponent()
        {
            this.lblMouseInputInfo = new System.Windows.Forms.Label();
            this.label1 = new System.Windows.Forms.Label();
            this.label2 = new System.Windows.Forms.Label();
            this.cbGestureNames = new System.Windows.Forms.ComboBox();
            this.tbGestureName = new System.Windows.Forms.TextBox();
            this.btnAddExistingType = new System.Windows.Forms.Button();
            this.btnAddNewType = new System.Windows.Forms.Button();
            this.label3 = new System.Windows.Forms.Label();
            this.btnDelete = new System.Windows.Forms.Button();
            this.label4 = new System.Windows.Forms.Label();
            this.cbRecognizer = new System.Windows.Forms.ComboBox();
            this.label5 = new System.Windows.Forms.Label();
            this.pbGestureSet = new System.Windows.Forms.PictureBox();
            this.pbDrawingArea = new System.Windows.Forms.PictureBox();
            this.panelQDollarSettings = new System.Windows.Forms.Panel();
            this.chkUseLowerBounding = new System.Windows.Forms.CheckBox();
            this.chkUseEarlyAbandoning = new System.Windows.Forms.CheckBox();
            this.btnClassificationTimeExperiment = new System.Windows.Forms.Button();
            this.cbLargeTrainingSets = new System.Windows.Forms.CheckBox();
            this.gbTimeAccuracyExperiment = new System.Windows.Forms.GroupBox();
            ((System.ComponentModel.ISupportInitialize)(this.pbGestureSet)).BeginInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbDrawingArea)).BeginInit();
            this.panelQDollarSettings.SuspendLayout();
            this.gbTimeAccuracyExperiment.SuspendLayout();
            this.SuspendLayout();
            // 
            // lblMouseInputInfo
            // 
            this.lblMouseInputInfo.AutoSize = true;
            this.lblMouseInputInfo.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.lblMouseInputInfo.Location = new System.Drawing.Point(449, 8);
            this.lblMouseInputInfo.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.lblMouseInputInfo.Name = "lblMouseInputInfo";
            this.lblMouseInputInfo.Size = new System.Drawing.Size(391, 16);
            this.lblMouseInputInfo.TabIndex = 1;
            this.lblMouseInputInfo.Text = "Make strokes on this canvas. Right-click the canvas to recognize.";
            // 
            // label1
            // 
            this.label1.AutoSize = true;
            this.label1.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label1.Location = new System.Drawing.Point(451, 414);
            this.label1.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label1.Name = "label1";
            this.label1.Size = new System.Drawing.Size(199, 16);
            this.label1.TabIndex = 3;
            this.label1.Text = "Add as exemple of existing type:";
            // 
            // label2
            // 
            this.label2.AutoSize = true;
            this.label2.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label2.Location = new System.Drawing.Point(451, 439);
            this.label2.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label2.Name = "label2";
            this.label2.Size = new System.Drawing.Size(197, 16);
            this.label2.TabIndex = 4;
            this.label2.Text = "Add as exemple of custom type:";
            // 
            // cbGestureNames
            // 
            this.cbGestureNames.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbGestureNames.FormattingEnabled = true;
            this.cbGestureNames.Items.AddRange(new object[] {
            "T",
            "N",
            "D",
            "P",
            "line",
            "five point star",
            "null",
            "arrowhead",
            "X",
            "H",
            "I",
            "exclamation",
            "pitchfork",
            "six point star",
            "asterisk",
            "half note"});
            this.cbGestureNames.Location = new System.Drawing.Point(692, 413);
            this.cbGestureNames.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.cbGestureNames.Name = "cbGestureNames";
            this.cbGestureNames.Size = new System.Drawing.Size(114, 20);
            this.cbGestureNames.TabIndex = 5;
            // 
            // tbGestureName
            // 
            this.tbGestureName.Location = new System.Drawing.Point(692, 439);
            this.tbGestureName.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.tbGestureName.Name = "tbGestureName";
            this.tbGestureName.Size = new System.Drawing.Size(114, 21);
            this.tbGestureName.TabIndex = 6;
            // 
            // btnAddExistingType
            // 
            this.btnAddExistingType.Location = new System.Drawing.Point(813, 412);
            this.btnAddExistingType.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnAddExistingType.Name = "btnAddExistingType";
            this.btnAddExistingType.Size = new System.Drawing.Size(83, 22);
            this.btnAddExistingType.TabIndex = 7;
            this.btnAddExistingType.Text = "Add";
            this.btnAddExistingType.UseVisualStyleBackColor = true;
            this.btnAddExistingType.Click += new System.EventHandler(this.btnAddExistingType_Click);
            // 
            // btnAddNewType
            // 
            this.btnAddNewType.Location = new System.Drawing.Point(813, 437);
            this.btnAddNewType.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnAddNewType.Name = "btnAddNewType";
            this.btnAddNewType.Size = new System.Drawing.Size(83, 22);
            this.btnAddNewType.TabIndex = 8;
            this.btnAddNewType.Text = "Add";
            this.btnAddNewType.UseVisualStyleBackColor = true;
            this.btnAddNewType.Click += new System.EventHandler(this.btnAddNewType_Click);
            // 
            // label3
            // 
            this.label3.AutoSize = true;
            this.label3.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label3.Location = new System.Drawing.Point(451, 466);
            this.label3.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label3.Name = "label3";
            this.label3.Size = new System.Drawing.Size(197, 16);
            this.label3.TabIndex = 9;
            this.label3.Text = "Delete all user-defined gestures";
            // 
            // btnDelete
            // 
            this.btnDelete.Location = new System.Drawing.Point(813, 462);
            this.btnDelete.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnDelete.Name = "btnDelete";
            this.btnDelete.Size = new System.Drawing.Size(83, 22);
            this.btnDelete.TabIndex = 10;
            this.btnDelete.Text = "Delete";
            this.btnDelete.UseVisualStyleBackColor = true;
            this.btnDelete.Click += new System.EventHandler(this.btnDelete_Click);
            // 
            // label4
            // 
            this.label4.AutoSize = true;
            this.label4.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label4.Location = new System.Drawing.Point(14, 8);
            this.label4.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label4.Name = "label4";
            this.label4.Size = new System.Drawing.Size(75, 16);
            this.label4.TabIndex = 11;
            this.label4.Text = "Gesture set";
            // 
            // cbRecognizer
            // 
            this.cbRecognizer.DropDownStyle = System.Windows.Forms.ComboBoxStyle.DropDownList;
            this.cbRecognizer.Font = new System.Drawing.Font("Microsoft Sans Serif", 8.25F, System.Drawing.FontStyle.Regular, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.cbRecognizer.ForeColor = System.Drawing.Color.Black;
            this.cbRecognizer.FormattingEnabled = true;
            this.cbRecognizer.Items.AddRange(new object[] {
            "$P",
            "$P+",
            "$Q"});
            this.cbRecognizer.Location = new System.Drawing.Point(653, 388);
            this.cbRecognizer.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.cbRecognizer.Name = "cbRecognizer";
            this.cbRecognizer.Size = new System.Drawing.Size(53, 21);
            this.cbRecognizer.TabIndex = 12;
            this.cbRecognizer.SelectedIndexChanged += new System.EventHandler(this.cbRecognizer_SelectedIndexChanged);
            // 
            // label5
            // 
            this.label5.AutoSize = true;
            this.label5.Font = new System.Drawing.Font("Microsoft Sans Serif", 9.75F, System.Drawing.FontStyle.Bold, System.Drawing.GraphicsUnit.Point, ((byte)(0)));
            this.label5.ForeColor = System.Drawing.Color.Green;
            this.label5.Location = new System.Drawing.Point(451, 389);
            this.label5.Margin = new System.Windows.Forms.Padding(4, 0, 4, 0);
            this.label5.Name = "label5";
            this.label5.Size = new System.Drawing.Size(166, 16);
            this.label5.TabIndex = 13;
            this.label5.Text = "Point-cloud recognizer:";
            // 
            // pbGestureSet
            // 
            this.pbGestureSet.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pbGestureSet.Image = global::PDollarDemo.Properties.Resources.multistrokes;
            this.pbGestureSet.Location = new System.Drawing.Point(14, 26);
            this.pbGestureSet.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.pbGestureSet.Name = "pbGestureSet";
            this.pbGestureSet.Size = new System.Drawing.Size(431, 351);
            this.pbGestureSet.SizeMode = System.Windows.Forms.PictureBoxSizeMode.StretchImage;
            this.pbGestureSet.TabIndex = 2;
            this.pbGestureSet.TabStop = false;
            // 
            // pbDrawingArea
            // 
            this.pbDrawingArea.BorderStyle = System.Windows.Forms.BorderStyle.FixedSingle;
            this.pbDrawingArea.Location = new System.Drawing.Point(454, 26);
            this.pbDrawingArea.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.pbDrawingArea.Name = "pbDrawingArea";
            this.pbDrawingArea.Size = new System.Drawing.Size(548, 351);
            this.pbDrawingArea.TabIndex = 0;
            this.pbDrawingArea.TabStop = false;
            this.pbDrawingArea.MouseDown += new System.Windows.Forms.MouseEventHandler(this.pbDrawingArea_MouseDown);
            this.pbDrawingArea.MouseMove += new System.Windows.Forms.MouseEventHandler(this.pbDrawingArea_MouseMove);
            this.pbDrawingArea.MouseUp += new System.Windows.Forms.MouseEventHandler(this.pbDrawingArea_MouseUp);
            // 
            // panelQDollarSettings
            // 
            this.panelQDollarSettings.Controls.Add(this.chkUseLowerBounding);
            this.panelQDollarSettings.Controls.Add(this.chkUseEarlyAbandoning);
            this.panelQDollarSettings.Location = new System.Drawing.Point(727, 388);
            this.panelQDollarSettings.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.panelQDollarSettings.Name = "panelQDollarSettings";
            this.panelQDollarSettings.Size = new System.Drawing.Size(272, 19);
            this.panelQDollarSettings.TabIndex = 14;
            // 
            // chkUseLowerBounding
            // 
            this.chkUseLowerBounding.AutoSize = true;
            this.chkUseLowerBounding.Checked = true;
            this.chkUseLowerBounding.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkUseLowerBounding.Location = new System.Drawing.Point(136, 3);
            this.chkUseLowerBounding.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkUseLowerBounding.Name = "chkUseLowerBounding";
            this.chkUseLowerBounding.Size = new System.Drawing.Size(111, 16);
            this.chkUseLowerBounding.TabIndex = 1;
            this.chkUseLowerBounding.Text = "lower bounding";
            this.chkUseLowerBounding.UseVisualStyleBackColor = true;
            // 
            // chkUseEarlyAbandoning
            // 
            this.chkUseEarlyAbandoning.AutoSize = true;
            this.chkUseEarlyAbandoning.Checked = true;
            this.chkUseEarlyAbandoning.CheckState = System.Windows.Forms.CheckState.Checked;
            this.chkUseEarlyAbandoning.Location = new System.Drawing.Point(5, 3);
            this.chkUseEarlyAbandoning.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.chkUseEarlyAbandoning.Name = "chkUseEarlyAbandoning";
            this.chkUseEarlyAbandoning.Size = new System.Drawing.Size(122, 16);
            this.chkUseEarlyAbandoning.TabIndex = 0;
            this.chkUseEarlyAbandoning.Text = "early abandoning";
            this.chkUseEarlyAbandoning.UseVisualStyleBackColor = true;
            // 
            // btnClassificationTimeExperiment
            // 
            this.btnClassificationTimeExperiment.BackColor = System.Drawing.Color.FromArgb(((int)(((byte)(255)))), ((int)(((byte)(224)))), ((int)(((byte)(192)))));
            this.btnClassificationTimeExperiment.Location = new System.Drawing.Point(7, 16);
            this.btnClassificationTimeExperiment.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.btnClassificationTimeExperiment.Name = "btnClassificationTimeExperiment";
            this.btnClassificationTimeExperiment.Size = new System.Drawing.Size(292, 37);
            this.btnClassificationTimeExperiment.TabIndex = 15;
            this.btnClassificationTimeExperiment.Text = "Run $P vs. $Q Time / Accuracy Experiment";
            this.btnClassificationTimeExperiment.UseVisualStyleBackColor = false;
            this.btnClassificationTimeExperiment.Click += new System.EventHandler(this.btnClassificationTimeExperiment_Click);
            // 
            // cbLargeTrainingSets
            // 
            this.cbLargeTrainingSets.AutoSize = true;
            this.cbLargeTrainingSets.Location = new System.Drawing.Point(8, 58);
            this.cbLargeTrainingSets.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.cbLargeTrainingSets.Name = "cbLargeTrainingSets";
            this.cbLargeTrainingSets.Size = new System.Drawing.Size(303, 16);
            this.cbLargeTrainingSets.TabIndex = 16;
            this.cbLargeTrainingSets.Text = "run test for large training sets (slower if checked)";
            this.cbLargeTrainingSets.UseVisualStyleBackColor = true;
            // 
            // gbTimeAccuracyExperiment
            // 
            this.gbTimeAccuracyExperiment.Controls.Add(this.btnClassificationTimeExperiment);
            this.gbTimeAccuracyExperiment.Controls.Add(this.cbLargeTrainingSets);
            this.gbTimeAccuracyExperiment.Location = new System.Drawing.Point(14, 382);
            this.gbTimeAccuracyExperiment.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.gbTimeAccuracyExperiment.Name = "gbTimeAccuracyExperiment";
            this.gbTimeAccuracyExperiment.Padding = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.gbTimeAccuracyExperiment.Size = new System.Drawing.Size(323, 95);
            this.gbTimeAccuracyExperiment.TabIndex = 17;
            this.gbTimeAccuracyExperiment.TabStop = false;
            this.gbTimeAccuracyExperiment.Text = " time / accuracy experiment";
            // 
            // FormMain
            // 
            this.AutoScaleDimensions = new System.Drawing.SizeF(7F, 12F);
            this.AutoScaleMode = System.Windows.Forms.AutoScaleMode.Font;
            this.ClientSize = new System.Drawing.Size(1013, 488);
            this.Controls.Add(this.gbTimeAccuracyExperiment);
            this.Controls.Add(this.panelQDollarSettings);
            this.Controls.Add(this.label5);
            this.Controls.Add(this.cbRecognizer);
            this.Controls.Add(this.label4);
            this.Controls.Add(this.btnDelete);
            this.Controls.Add(this.label3);
            this.Controls.Add(this.btnAddNewType);
            this.Controls.Add(this.btnAddExistingType);
            this.Controls.Add(this.tbGestureName);
            this.Controls.Add(this.cbGestureNames);
            this.Controls.Add(this.label2);
            this.Controls.Add(this.label1);
            this.Controls.Add(this.pbGestureSet);
            this.Controls.Add(this.lblMouseInputInfo);
            this.Controls.Add(this.pbDrawingArea);
            this.FormBorderStyle = System.Windows.Forms.FormBorderStyle.FixedSingle;
            this.Margin = new System.Windows.Forms.Padding(4, 3, 4, 3);
            this.Name = "FormMain";
            this.StartPosition = System.Windows.Forms.FormStartPosition.CenterScreen;
            this.Text = "$P, $P+, and $Q Demo (June 2018)";
            ((System.ComponentModel.ISupportInitialize)(this.pbGestureSet)).EndInit();
            ((System.ComponentModel.ISupportInitialize)(this.pbDrawingArea)).EndInit();
            this.panelQDollarSettings.ResumeLayout(false);
            this.panelQDollarSettings.PerformLayout();
            this.gbTimeAccuracyExperiment.ResumeLayout(false);
            this.gbTimeAccuracyExperiment.PerformLayout();
            this.ResumeLayout(false);
            this.PerformLayout();

        }

        #endregion

        private System.Windows.Forms.PictureBox pbDrawingArea;
        private System.Windows.Forms.Label lblMouseInputInfo;
        private System.Windows.Forms.PictureBox pbGestureSet;
        private System.Windows.Forms.Label label1;
        private System.Windows.Forms.Label label2;
        private System.Windows.Forms.ComboBox cbGestureNames;
        private System.Windows.Forms.TextBox tbGestureName;
        private System.Windows.Forms.Button btnAddExistingType;
        private System.Windows.Forms.Button btnAddNewType;
        private System.Windows.Forms.Label label3;
        private System.Windows.Forms.Button btnDelete;
        private System.Windows.Forms.Label label4;
        private System.Windows.Forms.ComboBox cbRecognizer;
        private System.Windows.Forms.Label label5;
        private System.Windows.Forms.Panel panelQDollarSettings;
        private System.Windows.Forms.CheckBox chkUseLowerBounding;
        private System.Windows.Forms.CheckBox chkUseEarlyAbandoning;
        private System.Windows.Forms.Button btnClassificationTimeExperiment;
        private System.Windows.Forms.CheckBox cbLargeTrainingSets;
        private System.Windows.Forms.GroupBox gbTimeAccuracyExperiment;
    }
}

