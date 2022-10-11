d = DslBezier()

d.position_pen(2,2)
d.straight_line(Direction.NE, Length.long)
d.curve(Direction.W, Orient.right, Length.medium, Radius.medium)
d.straight_line(Direction.S, Length.medium)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.S, Orient.right, Length.short, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)

d.end()
