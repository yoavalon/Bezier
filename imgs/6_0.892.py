d = DslBezier()

d.position_pen(1,3)
d.curve(Direction.S, Orient.left, Length.medium, Radius.low)
d.curve(Direction.E, Orient.right, Length.long, Radius.medium)
d.position_pen(1,1)
d.straight_line(Direction.SE, Length.long)
d.curve(Direction.SW, Orient.left, Length.short, Radius.medium)
d.straight_line(Direction.E, Length.short)

d.end()
