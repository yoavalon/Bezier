d = DslBezier()

d.position_pen(2,1)
d.curve(Direction.SE, Orient.left, Length.short, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.S, Length.short)
d.straight_line(Direction.SW, Length.long)
d.curve(Direction.E, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.NE, Orient.right, Length.long, Radius.low)

d.end()
