d = DslBezier()

d.position_pen(1,1)
d.curve(Direction.SW, Orient.left, Length.medium, Radius.medium)
d.straight_line(Direction.SW, Length.short)
d.straight_line(Direction.SE, Length.medium)
d.curve(Direction.NW, Orient.left, Length.medium, Radius.medium)
d.curve(Direction.W, Orient.right, Length.long, Radius.medium)
d.straight_line(Direction.SE, Length.medium)

d.end()
