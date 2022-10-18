d = DslBezier()

d.position_pen(0,3)
d.straight_line(Direction.E, Length.long)
d.position_pen(2,2)
d.curve(Direction.SE, Orient.right, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.medium)
d.curve(Direction.W, Orient.right, Length.short, Radius.low)

d.end()
