d = DslBezier()

d.position_pen(3,3)
d.curve(Direction.NW, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.long)
d.straight_line(Direction.SE, Length.medium)
d.straight_line(Direction.E, Length.short)
d.position_pen(1,2)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.short, Radius.medium)

d.end()
