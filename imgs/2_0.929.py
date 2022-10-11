d = DslBezier()

d.position_pen(2,0)
d.curve(Direction.SE, Orient.right, Length.long, Radius.low)
d.curve(Direction.SE, Orient.left, Length.long, Radius.medium)
d.position_pen(0,2)
d.curve(Direction.S, Orient.right, Length.medium, Radius.low)
d.straight_line(Direction.SW, Length.medium)

d.end()
