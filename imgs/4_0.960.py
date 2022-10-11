d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.short, Radius.low)
d.curve(Direction.W, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.NE, Length.long)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.NE, Orient.left, Length.long, Radius.medium)
d.position_pen(0,1)

d.end()
