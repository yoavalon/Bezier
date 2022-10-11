d = DslBezier()

d.position_pen(2,3)
d.position_pen(0,1)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.straight_line(Direction.NE, Length.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
