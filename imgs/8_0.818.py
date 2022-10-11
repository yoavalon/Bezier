d = DslBezier()

d.position_pen(0,0)
d.straight_line(Direction.S, Length.medium)
d.position_pen(1,1)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.curve(Direction.S, Orient.left, Length.long, Radius.medium)
d.curve(Direction.SE, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)

d.end()
